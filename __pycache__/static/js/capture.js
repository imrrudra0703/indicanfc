// CAMERA SETTINGS.
    Webcam.set({
        width: 220,
        height: 190,
        image_format: 'jpeg',
        jpeg_quality: 100
    });
    Webcam.attach('#camera');

    // TAKE A SNAPSHOT.
    takeSnapShot = function () {
        Webcam.snap(function (data_uri) {
            downloadImage('indican', data_uri);
        });
    }

    // DOWNLOAD THE IMAGE.
    downloadImage = function (name, datauri) {
        var a = document.createElement('a');
        a.setAttribute('download', name + '.png');
        a.setAttribute('href', datauri);
        a.click();
    }
