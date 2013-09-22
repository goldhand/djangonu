'use strict';

/* Services */

angular.module('essaysServices', ['ngResource']).
    factory('Essay', function($resource){
  return $resource('/api/essay/:essayId/', {}, {
    query: {method:'GET', params:{essayId:''}, isArray:false}
  });
});