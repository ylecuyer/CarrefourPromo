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
				when('/crf_express', {
					templateUrl: 'partials/crf_express.html',
					controller: 'ListingCtrl'
				}).
				when('/crf_city', {
					templateUrl: 'partials/crf_city.html',
					controller: 'ListingCtrl'
				}).
				when('/crf_contact', {
					templateUrl: 'partials/crf_contact.html',
					controller: 'ListingCtrl'
				}).
				when('/crf_montagne', {
					templateUrl: 'partials/crf_montagne.html',
					controller: 'ListingCtrl'
				}).
				otherwise({
					redirectTo: '/home'
				});
			}]);

