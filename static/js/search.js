app.controller('search',function($scope,$cookies,$http,Upload,toaster){

    $scope.loadlistoffiles=function(){
        if(!$cookies.get("parentid") || $cookies.get("parentid").length == 0){
            $cookies.put("parentid" , "/");
        }
        var req_obj = {
            "folderid" : $cookies.get("parentid")
        }
        return $http.post('/api/getchildren', req_obj).then(function(response,status){
            $scope.filedata=response.data;
            $scope.listoffiles=$scope.filedata.reverse()
        });
    }

    $scope.deleteconfirmation=function(file){
        var element = angular.element('#deletefileconfirmation');
        element.modal('show');
        $scope.deletefileid=file.fileid
        $scope.deletefiletype=file.filetype
    }

    $scope.deletefile=function(){

        return $http.get('/api/deletefile?id='+$scope.deletefileid).then(function(response,status){
            $scope.listoffiles=response.data;
            $scope.loadlistoffiles();
            toaster.pop('success','File successfully deleted')
        });
    }

    $scope.renameconfirmation=function(file){
        var element = angular.element('#renamefile');
        element.modal('show');
        $scope.filetoberenamed=file.filename;
        $scope.fileidofrenamedfile=file.fileid;
    }

    $scope.getfoldername=function(file){
        var element = angular.element('#getfoldername');
        element.modal('show');
    }

    $scope.showinfomodal=function(file){
        var element = angular.element('#fileinfomodal');
        element.modal('show');
        $scope.infofile=file;
    }

    $scope.renamefile=function(){
        $scope.datatobesent={}
        $scope.datatobesent['filerename']=$scope.filetoberenamed
        $scope.datatobesent['fileid']=$scope.fileidofrenamedfile
        return $http.post('/api/rename',$scope.datatobesent).then(function(response,status){
            $scope.listoffiles=response.data;
            toaster.pop('success','File successfully rename')
            $scope.filetoberenamed='';
            $scope.fileidofrenamedfile='';
            $scope.loadlistoffiles();
        });
    }

    $scope.createfolder=function(){
        if(!$cookies.get("parentid") || $cookies.get("parentid").length == 0){
            $cookies.put("parentid" , "/");
        }
        var req_obj = {
            "parentid" : $cookies.get("parentid"),
            "folderlist": [$scope.foldername]
        }
        $scope.activategif=true;
        return $http.post('/api/createfolder',req_obj).then(function(response,status){
            $scope.activategif=false;
            toaster.pop('success','Folder successfully created')
            $scope.loadlistoffiles();
        });
    }

    $scope.selected = 'None';




    $scope.loadlistoffiles();

    $scope.uploadfile=function(){
            files=$scope.files
            if(!$cookies.get("parentid") || $cookies.get("parentid").length == 0){
                $cookies.put("parentid" , "/");
            }
            if(files!=null){
                    $scope.activategif=true;
                    Upload.upload({
                        url: '/api/upload',
                        method:'POST',
                        data:{files:files, "parentid" : $cookies.get("parentid")}
                    }).success(function (resp) {
                        $scope.activategif=false;
                        console.log("Hello")
                        toaster.pop('success','File upload successful!')
                    }, function (resp) {
                        toaster.pop('fail','Uploading '+files.filename+' failed due to'+resp.status)
                        //console.log('Error status: ' + resp.status);
                    }, function (evt) {
                        var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                        console.log('progress: ' + progressPercentage + '% ' + evt.config.data.file.name);
                    }).finally(function(){
                        $scope.loadlistoffiles()
                        $scope.activategif=false;
                    });
            }
    }



    $scope.menuOptions = [
        // NEW IMPLEMENTATION
        {
            text:'Rename',
            click: function($itemScope, $event, modelValue, text, $li){
                $scope.renameconfirmation($itemScope.files);
            }
        },{
            text: 'Delete',
            click: function ($itemScope, $event, modelValue, text, $li) {
                $scope.deleteconfirmation($itemScope.files);
            }
        },{
            text: 'Info',
            click: function ($itemScope, $event, modelValue, text, $li) {
                $scope.showinfomodal($itemScope.files);
            }
        }
    ];

});
