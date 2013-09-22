'use strict';

/* App Module */

var essays = angular.module('essays', ['essaysServices', 'ngRoute', 'ngAnimate', 'ngCookies']);

essays.config(function($interpolateProvider, $routeProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
    $routeProvider.
        when('/essays', {templateUrl: '/api/angular/partials/essay-list/'}).
        when('/essays/:essayId', {templateUrl: '/api/angular/partials/essay-detail/'}).
        when('/document/:essayId', {templateUrl: '/api/angular/partials/essay-document/'}).
        when('/users/:userId', {templateUrl: '/api/angular/partials/essay-list/'}).
        otherwise({redirectTo: '/document/'});
});

essays.run(function($rootScope, $log, $http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


//essays.config(function($routeProvider) {
//    $routeProvider.
//        when('/essays', {templateUrl: '/api/angular/partials/essay-list/'}).
//        when('/essays/:essayId', {templateUrl: '/api/angular/partials/essay-detail/'}).
//        otherwise({redirectTo: '/essays'});
//});
