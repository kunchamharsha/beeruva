app=angular.module('app',['ngFileUpload','ui.bootstrap.contextMenu','toaster'])
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[{[');
    $interpolateProvider.endSymbol(']}]');
});

app.directive('ngRightClick', function($parse) {
    return function(scope, element, attrs) {
        var fn = $parse(attrs.ngRightClick);
        element.bind('contextmenu', function(event) {
            scope.$apply(function() {
                event.preventDefault();
                fn(scope, {$event:event});
            });
        });
    };
});