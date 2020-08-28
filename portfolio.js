var app = angular.module("PortfolioApp", ["ngRoute"]);

    app.config(function($routeProvider) {
        $routeProvider.when("/", {
            templateUrl : "partials/home.html"
        })
        .when("/artwork", {
            templateUrl : "partials/artwork.html"
        })
        .otherwise({
            templateUrl : "partials/home.html"
        })
    });