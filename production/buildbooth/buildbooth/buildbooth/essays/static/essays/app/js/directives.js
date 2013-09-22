'use strict';

/* Directives */
essays.directive('essayBlur', function () {
	return function (scope, elem, attrs) {
		elem.bind('blur', function () {
			scope.$apply(attrs.essayBlur);
		});
	};
});
