'use strict';

/* Controllers */

essays.controller('EssayListCtrl', function EssayListCtrl($scope, $routeParams, $http) {
    $http.get('/api/essay/').success(function(data) {
        $scope.essays = data;
    });

    $scope.orderProp = 'created';
});


essays.controller('EssayListCtrl', function EssayListCtrl($scope, $routeParams, $http) {

    $scope.essays = [];
    var essays_url = '/api/essay/';

    if ($routeParams.userId) {
        essays_url = '/api/users/' + $routeParams.userId + '/';
        $http.get(essays_url).success(function(data) {
            for (var i = 0; i < data.essays.length; i++) {
                $http.get(data.essays[i]).success(function(essay_data) {
                    $scope.essays.push(essay_data);
                });
            }
            $scope.user = data.username;
        });

    } else {
        $http.get(essays_url).success(function(data) {
            $scope.essays = data;
        });
    }

    $scope.orderProp = 'created';
});

//PhoneListCtrl.$inject = ['$scope', '$http'];


essays.controller('EssayDetailCtrl', function EssayDetailCtrl($scope, $routeParams, $http) {
    $scope.body = [];
    $http.get('/api/essay/' + $routeParams.essayId + '/').success(function(data) {
        $scope.essay = data;
        if (data.intro[0]) {
            $http.get(data.intro[0]).success(function(intro_data) {
                $scope.intro = intro_data;
            });
        }
        if (data.body) {
            for (var i = 0; i < $scope.essay.body.length; i++) {
                $http.get($scope.essay.body[i]).success(function(body_data) {
                    $scope.body.push(body_data);
                });
            }
        }
        if (data.conclusion[0]) {
            $http.get(data.conclusion[0]).success(function(conclusion_data) {
                $scope.conclusion = conclusion_data;
            });
        }
    });
    $scope.orderProp = 'created';
});

essays.controller('DocumentCtrl', function DocumentCtrl($scope, $routeParams, $http) {

    $scope.essay = {};
    $scope.bodyParagraph =
    {
        intro: '',
        transition: '',
        body: '',
        conclusion: ''
    };
    $scope.document = {
        essay: {
            title: ''
        },
        intro: {
            intro: '',
            transition: '',
            thesis: '',
            conclusion: ''
        },
        body: [],
        conclusion: {
            intro: '',
            thesisTransition: '',
            thesis: '',
            body: '',
            conclusion: ''
        }
    };
    if ($routeParams.essayId != undefined) {
        $http.get('/api/essay/' + $routeParams.essayId + '/').success(function(data) {
            $scope.essay = data;
            $scope.document.essay = data;
            if (data.intro[0]) {
                $http.get(data.intro[0]).success(function(intro_data) {
                    $scope.document.intro = intro_data;
                });
            }
            if (data.body) {
                for (var i = 0; i < $scope.essay.body.length; i++) {
                    $http.get($scope.essay.body[i]).success(function(body_data) {
                        $scope.document.body.push(body_data);
                    });
                }
            }
            if (data.conclusion[0]) {
                $http.get(data.conclusion[0]).success(function(conclusion_data) {
                    $scope.document.conclusion = conclusion_data;
                });
            }
        });
    }

    $scope.saveIntro = function () {

        var intro_url = '/api/intro/';
        if ($scope.document.intro.url) {
            intro_url = $scope.document.intro.url;
            $http.put(
                intro_url,
                $scope.document.intro
            );
        } else {
            $scope.document.intro.essay = $scope.essay.url;
            $http.post(
                    intro_url,
                    $scope.document.intro
                ).success(function(data) {
                    $scope.document.intro = data;
                });
        };
    };

    $scope.saveConclusion = function () {

        var conclusion_url = '/api/conclusion/';
        if ($scope.document.conclusion.url) {
            conclusion_url = $scope.document.conclusion.url;
            $http.put(
                conclusion_url,
                $scope.document.conclusion
            );
        } else {
            $scope.document.conclusion.essay = $scope.essay.url;
            $http.post(
                    conclusion_url,
                    $scope.document.conclusion
                ).success(function(data) {
                    $scope.document.conclusion = data;
                });
        };
    };

    $scope.saveBody = function () {

        var body_url = '/api/body/';
        if ($scope.bodyParagraph.id) {
            body_url += $scope.bodyParagraph.id + '/';
            $http.put(
                body_url,
                $scope.bodyParagraph
            );
            $('#body-paragraph').show();
        } else {
            $scope.bodyParagraph.essay = $scope.essay.url;
            $http.post(
                body_url,
                $scope.bodyParagraph
            ).success(function(data) {
                    $scope.document.body.push(data);
                });
        };
        $scope.bodyParagraph =
        {
            intro: '',
            transition: '',
            body: '',
            conclusion: ''
        };
    };
    $scope.editBody = function (bodyParagraph) {
        $scope.bodyParagraph = bodyParagraph;
        $('#body-paragraph').hide();
    };
    $scope.saveEssay = function () {

        var essay_url = '/api/essay/';
        if (this.document.essay.url) {
            essay_url = this.document.essay.url;
            $http.put(
                essay_url,
                this.document.essay
            );
        } else {
            $http.post(
                essay_url,
                {
                    'title': this.document.essay.title
                }
            ).success(function(data) {
                    $scope.document.essay.id = data.id;
                    $scope.essay.id = data.id;
                    $scope.essay.url = data.url;
                });
        }
    };
    $('input').each(function() {
        $(this).popover({
                placement: 'right',
                html: true,
                trigger: 'focus'

            }
        );
    });
    $('textarea').each(function() {
        $(this).popover({
                placement: 'right',
                html: true,
                trigger: 'focus'

            }
        );
    });
});

//PhoneDetailCtrl.$inject = ['$scope', '$routeParams'];

function AuthorCtrl($scope, $http) {
    $http.get('/static/author/author.json').success(function(data) {
        $scope.author = data;
    });
}


