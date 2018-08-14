angular.module('MyApp', [])
    .controller('displayController', function($scope, $http) {
        $http.get("http://127.0.0.1:8000/emp/").success(function (response) {
        $scope.datas = response;
    });
});