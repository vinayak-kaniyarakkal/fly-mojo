var Upload = function (file) {
    this.file = file;
};

Upload.prototype.getType = function() {
    return this.file.type;
};
Upload.prototype.getSize = function() {
    return this.file.size;
};
Upload.prototype.getName = function() {
    return this.file.name;
};
Upload.prototype.doUpload = function (fn) {
    var that = this;
    var formData = new FormData();

    // add assoc key values, this will be posts values
    formData.append("image", this.file, this.getName());
    formData.append("name", this.getName());

    console.log(this.file);

    $.ajax({
        type: "POST",
        url: "/upload/",
        xhr: function () {
            var myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) {
                myXhr.upload.addEventListener('progress', that.progressHandling, false);
            }
            return myXhr;
        },
        success: function (data) {
            // your callback here
            fn(data);
        },
        error: function (error) {
            // handle error
        },
        async: true,
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        timeout: 60000
    });
};

Upload.prototype.progressHandling = function (event) {
    var percent = 0;
    var position = event.loaded || event.position;
    var total = event.total;
    var progress_bar_id = "#progress-wrp";
    if (event.lengthComputable) {
        percent = Math.ceil(position / total * 100);
    }
    // update progressbars classes so it fits your code
    $(progress_bar_id + " .progress-bar").css("width", +percent + "%");
    $(progress_bar_id + " .status").text(percent + "%");
};

$(document).ready(function(){

    var body = $(document.body).tags({
        '.uploadBox':{
            '.imgBox':{},
            '.img.material-icons':{
                $:{
                    text:'photo_size_select_actual'
                }
            },'.btn':{
                $:{
                    text:'Upload Pan Image'
                },
                'input.fileUpload':{
                    $:{
                        attr:{
                            type:'file',
                            style:'position: absolute;cursor: pointer;width: 400%;height: 400%;left: -50%;opacity: 0;padding: 0;margin: 0;top: -50%;'
                        }
                    }
                }
            }
        }
    });

    $('.fileUpload').change(function(e){
        var file = $(this)[0].files[0];
        file = new Upload(file);
        file.doUpload(function(){
            $(body.uploadBox.$element).remove();
            stepTwo(file.getName());
        });
    });


    function stepTwo(name) {
        $(document.body).tags({
            '.uploadBox':{
                '.imgurl':{
                    $:{
                        css:{
                            'background-image':'url("./img/'+name+'")'
                        }
                    }
                },'.line':{
                    $:{
                        css:{
                            'margin-top':'25px'
                        }
                    },
                    'input':{},
                    '.name':{
                        $:{
                            text:'Name'
                        }
                    },
                },'.line.a':{
                    'input':{},
                    '.name':{
                        $:{
                            text:'Birth Date'
                        }
                    },
                },'.line.b':{
                    'input':{},
                    '.name':{
                        $:{
                            text:'Pan No.'
                        }
                    },
                },'.btn':{
                    $:{
                        text:'Submit'
                    }
                }
            }
        });
    }

    //stepTwo('2048cutemonstersdribble.jpg');
});