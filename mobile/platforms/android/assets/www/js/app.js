var CPApp = angular.module('CPApp', [
		'ngRoute',
		'CPControllers'
]);

CPApp.config(['$routeProvider',
		function($routeProvider) {
			$routeProvider.
				when('/home', {
					templateUrl: 'partials/home.html',
					controller: 'HomeCtrl'
				}).
				otherwise({
					redirectTo: '/home'
				});
			}]);

