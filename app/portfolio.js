var app = angular.module("PortfolioApp", ["ngRoute"]);

app.config(function($routeProvider) {
    $routeProvider.when("/", {
        templateUrl : "partials/home.html"
    })
    .when("/artwork", {
        templateUrl : "partials/artwork.html",
        controller: "artworkCtrl"
    })
    .when("/about", {
        templateUrl : "partials/about.html",
        controller: "aboutCtrl"
    })
    .when("/contact", {
        templateUrl : "partials/contact.html",
        controller: "contactCtrl"
    })
    .when("/data", {
        templateUrl : "partials/data.html",
        controller: "dataCtrl"
    })
    .otherwise({
        templateUrl : "partials/home.html"
    })
});