$(function() {
	var REFRESH_SPIDERS_INFO_INTERVAL = 1 * 1000; // seconds
	var EPOCH_TIME = moment('1970/01/01');


	var ScraperManager = function (project) {

		var instance = {

			// SCRAPYD_BASE_URL: 'http://localhost:6800/',
			SCRAPYD_BASE_URL: 'http://veritza.herokuapp.com:6800/',

			defaultAJAXOptions: {
				method: 'GET',
				dataType: 'json',
				params: {},
				success: function () {},
				error: function (errorText) {
					console.log(errorText);
				},
			},

			_projects: null,
			_spiders: null,
			_jobs: {},

			spiders: {},

			listProjects: function () {
				var self = this;

				this._sendRequest('listprojects', {
					success: function (data) {
						self._projects = data.projects || [];
					},
					error: function (errorText) {
						console.log(errorText);
					}
				});
			},

			listSpiders: function (project, callback) {
				var self = this;
				project = project || this.project;

				this._sendRequest('listspiders', {
					params: {
						project: project
					},
					success: function (data) {
						self._spiders = data.spiders || [];

						if (typeof callback === 'function') {
							callback.bind(self)();
						}
					},
					error: function (errorText) {
						console.log(errorText);
					}
				});
			},

			listJobs: function (project, callback) {
				var self = this;
				project = project || this.project;

				this._sendRequest('listjobs', {
					params: {
						project: project
					},
					success: function (data) {
						self._jobs.finished = data.finished || [];
						self._jobs.pending = data.pending || [];
						self._jobs.running = data.running || [];
						self.updateSpidersData();

						if (typeof callback === 'function') {
							callback.bind(self)();
						}
					},
					error: function (errorText) {
						console.log(errorText);
					}
				});
			},

			schedule: function (spider, project) {
				project = project || this.project;

				this._sendRequest('schedule', {
					method: 'POST',
					params: {
						project: project,
						spider: spider
					},
					success: function (data) {
						console.log('scheduled');
						$.event.trigger('spider:scheduled');
					},
					error: function (errorText) {
						console.log(errorText);
					}
				});
			},

			cancel: function (job, project) {
				project = project || this.project;

				this._sendRequest('cancel', {
					method: 'POST',
					params: {
						project: project,
						job: job
					},
					success: function (data) {
						console.log('canceled');
						$.event.trigger('spider:canceled');
					},
					error: function (errorText) {
						console.log(errorText);
					}
				});
			},

			// Updates current spiders info based on the latest data about jobs
			// fetched with listJobs()
			updateSpidersData: function () {
				var self = this,
					spiders = {};

				this._spiders.forEach(function (spider) {
					spiders[spider] = {
						status: 'finished',
						lastRun: '',
						jobid: ''
					}

					// check for spider in 'running' jobs
					for (var i in self._jobs.running) {

						var job = self._jobs.running[i];
						if (spider === job.spider) {
							spiders[job.spider] = {
								status: 'running',
								lastRun: moment(job.start_time),
								jobid: job.id
							}
							// spider is found in 'running' jobs, don't surch anymore
							return;
						}
					}


					// check for spider in 'pending' jobs if not found in 'running' jobs
					for (var i in self._jobs.pending) {

						var job = self._jobs.pending[i];
						if (spider === job.spider) {
							spiders[job.spider] = {
								status: 'pending',
								lastRun: moment(job.start_time),
								jobid: job.id
							}
							// spider is found in 'pending' jobs, don't search anymore
							return;
						}
					}


					var last_end_time = EPOCH_TIME;
					// finally check for spider in 'finished' jobs if not found in 'running' or 'pending' jobs
					for (var i in self._jobs.finished) {

						var job = self._jobs.finished[i];
						if (spider === job.spider) {

							// get the latest time the spider was ran
							var job_end_time = moment(job.end_time);
							if (last_end_time < job_end_time) {
								last_end_time = job_end_time;
							}

							spiders[job.spider] = {
								status: 'finished',
								lastRun: last_end_time,
								jobid: job.id
							}
						}
					}
				});

				this.spiders = spiders;
			},

			updateSpidersInfo: function () {
				var self = this;
				this.listJobs(this.project, function () {
					for (var spider in self.spiders) {
						self._updateSpiderStatus(spider, self.project);
						self._updateSpiderAction(spider, self.project);
						self._updateSpiderLastRun(spider, self.project);
					}
				});
			},

			_updateSpiderStatus: function (spider, project) {
				var $statusElement = $('#project-' + project + ' #spider-' + spider + ' #spider-status');
				$statusElement.removeClass('label-success').removeClass('label-warning').removeClass('label-primary');

				switch(this.spiders[spider].status) {
					case 'running':
						$statusElement.addClass('label-success');
						break;

					case 'pending':
						$statusElement.addClass('label-warning');
						break;

					case 'finished':
					default:
						$statusElement.addClass('label-primary');
						break;
				}

				$statusElement.html(this.spiders[spider].status);
			},

			_updateSpiderAction: function (spider, project) {
				var $actionElement = $('#project-' + project + ' #spider-' + spider + ' #spider-action');
				var jobid = this.spiders[spider].jobid;
				$actionElement.removeClass('btn-success').removeClass('btn-danger');

				if ($actionElement) {
					switch(this.spiders[spider].status) {
						case 'running':
							$actionElement.addClass('btn-danger');
							$actionElement.html('Stop');
							$actionElement[0].onclick = this.cancel.bind(this, jobid, project);
							break;

						case 'pending':
							$actionElement.addClass('btn-danger');
							$actionElement.html('Stop');
							$actionElement[0].onclick = this.cancel.bind(this, jobid, project);
							break;

						case 'finished':
							$actionElement.addClass('btn-success');
							$actionElement.html('Run');
							$actionElement[0].onclick = this.schedule.bind(this, spider, project);
						default:
							break;
					}
				}
			},

			_updateSpiderLastRun: function (spider, project) {
				var $lastRunElement = $('#project-' + project + ' #spider-' + spider + ' #spider-last-run'),
					lastRun = moment(this.spiders[spider].lastRun),
					lastRunLabel = '-';

				if (lastRun.isValid()) {
					lastRunLabel = lastRun.format("MMM Do YYYY, h:mm A");
				}

				$lastRunElement.html(lastRunLabel);
			},

			_sendRequest: function (action, options) {
				options = $.extend({}, this.defaultAJAXOptions, options);

				return $.ajax({
					url: this.SCRAPYD_BASE_URL + action + '.json',
					method: options.method,
					data: options.params,
					dataType: options.dataType,
					success: options.success,
					error: options.error
				});
			}
		}

		if (project) {
			instance.project = project;
		}
		return instance;
	}

	window.ScraperManager = ScraperManager;

	manager = new ScraperManager('montenegro');

	// Spiders need to be fetched first so updateSpiderData() can work properly
	manager.listSpiders('montenegro', function () {
		manager.updateSpidersInfo();
	});
	setInterval(manager.updateSpidersInfo.bind(manager), REFRESH_SPIDERS_INFO_INTERVAL);
});

