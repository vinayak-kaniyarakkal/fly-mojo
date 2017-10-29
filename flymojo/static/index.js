var UploadHandler = function (file) {
    this.file = file;
};

UploadHandler.prototype.getType = function() {
    return this.file.type;
};
UploadHandler.prototype.getSize = function() {
    return this.file.size;
};
UploadHandler.prototype.getName = function() {
    return this.file.name;
};

UploadHandler.prototype.doUpload = function (fn) {
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

UploadHandler.prototype.progressHandling = function (event) {
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
            $:{
                each:function(elm) {
                    $(elm).addClass('hide');
                    setTimeout(function(){
                        $(elm).removeClass('hide');
                    },200);
                }
            },
            '.imgBox':{},
            '.img.material-icons':{
                $:{
                    text:'photo_size_select_actual'
                }
            },'.btn':{
                $:{
                    text:'Upload Pancard Image'
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
        file = new UploadHandler(file);
        file.doUpload(function(){
            $(body.uploadBox.$element).remove();
            animateNext(file.getName());
        });
        animateNext('2048cutemonstersdribble.jpg');
    });

    var checkBtnFn = function(elm,fn){
        $(elm).addClass('material-icons');
        $(elm).click(function(){
            if($(elm).hasClass('ok')){
                $(elm).removeClass('ok');
                $(elm).text('');
                fn(false);
            }else{
                $(elm).addClass('ok');
                $(elm).text('done');
                fn(true)
            }
        });
    }

    var FBdata = {
        name:{
            value:undefined,
            mark:false
        },birth_date:{
            value:undefined,
            mark:false
        },pan_no:{
            value:undefined,
            mark:false
        }
    };

    function sendFeedback(){
        console.log(FBdata);
        var formData = new FormData();
        formData.append("FBdata", JSON.stringify(FBdata));
        $.ajax({
            type: "POST",
            url: "/sendFeedback/",
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
    }

    function animateNext(name) {
        $(body.uploadBox.$element).addClass('go');
        setTimeout(function(){
            stepTwo(name);
        },200);
    }

    function stepTwo(name) {
        $(document.body).html('');
        var div = $(document.body).tags({
            '.uploadBox':{
                $:{
                    each:function(elm) {
                        $(elm).addClass('hide');
                        setTimeout(function(){
                            $(elm).removeClass('hide');
                        },200);
                    },
                    css:{
                        height:'648px'
                    }
                },
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
                    'input':{
                        $: {
                            val: 'Kishan Devani',
                            each: function (elm) {
                                $(elm).on('input propertychange paste', function () {
                                    FBdata.name.value = $(this).val();
                                });
                            }
                        }
                    },
                    '.name':{
                        $:{
                            text:'Name'
                        }
                    },'.check':{
                        $:{
                            each:function (elm) {
                                new checkBtnFn(elm,function (val) {
                                    FBdata.name.mark = val;
                                });
                            }
                        }
                    }
                },'.line.a':{
                    'input':{
                        $: {
                            val: '10/12/2017',
                            each: function (elm) {
                                $(elm).on('input propertychange paste', function () {
                                    FBdata.name.value = $(this).val();
                                });
                            }
                        }
                    },
                    '.name':{
                        $:{
                            text:'Birth Date'
                        }
                    },'.check':{
                        $:{
                            each:function (elm) {
                                new checkBtnFn(elm,function (val) {
                                    FBdata.birth_date.mark = val;
                                });
                            }
                        }
                    }
                },'.line.b':{
                    'input':{
                        $:{
                            val: '895 68 959 68',
                            each: function (elm) {
                                $(elm).on('input propertychange paste', function () {
                                    FBdata.name.value = $(this).val();
                                });
                            }
                        }
                    },
                    '.name':{
                        $:{
                            text:'Pan No.'
                        }
                    },'.check':{
                        $:{
                            each:function (elm) {
                                new checkBtnFn(elm,function (val) {
                                    FBdata.pan_no.mark = val;
                                });
                            }
                        }
                    }
                },'.line.c':{
                    $:{
                        css:{
                            height:'auto'
                        }
                    },
                    '.note':{
                        'span.material-icons':{
                            $:{
                                text:'info'
                            }
                        },'span':{
                            $:{
                                text:'Tap on mark if field value is correct or edit it.'
                            }
                        }
                    }
                },'.btn':{
                    $:{
                        text:'Submit',
                        each:function(elm){
                            $(elm).click(function(){
                                $(div.uploadBox.$element).addClass('go');
                                setTimeout(function(){
                                    $(document.body).html('');
                                    done();
                                },200);
                            });
                        }
                    }
                }
            }
        });
    }

    function done(){
        var body = $(document.body).tags({
            '.uploadBox':{
                $:{
                    each:function(elm) {
                      $(elm).addClass('hide');
                      setTimeout(function(){
                            $(elm).removeClass('hide');
                      },200);
                    },
                    css:{
                        height:'200px',
                        overflow:'visible'
                    }
                },
                '.imgBox':{
                    $:{
                        css:{
                            height:'100%'
                        }
                    },'.img.material-icons':{
                        $:{
                            text:'done',
                            css:{
                                color:'#00CC66'
                            }
                        }
                    }
                },
                '.doneText':{
                    $:{
                        text:'Submitted Successfully.'
                    }
                }
            }
        });
    }

    //animateNext('2048cutemonstersdribble.jpg');


});