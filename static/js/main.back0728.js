const init = async () => {
    //HTML要素の取得
    const startButton = document.querySelector("button#start"); 
    const shotButton = document.querySelector("button#shot");
    const audioDeviceSelect = document.getElementById("audio-devices");
    const videoDeviceSelect = document.getElementById("video-devices");
    const videoContainer = document.getElementById("stream");
    const canvasContainer = document.getElementById("screenshot");
    var img = document.getElementById('img');
  
    await navigator.mediaDevices.getUserMedia({video: {width:	1600,
      height:	 900,}, audio: true});

    //デバイスのリストを作成
    const devices = await navigator.mediaDevices.enumerateDevices();
    devices.forEach((device) => {
      console.log(device.kind + ": " + device.label + " id = " + device.deviceId);
      const option = document.createElement("option");
      option.text = device.label;
      option.value = device.deviceId;

      if (device.kind === "audioinput") {
        audioDeviceSelect.appendChild(option);
      } else if (device.kind === "videoinput") {
        videoDeviceSelect.appendChild(option);
      }
    });
  
    const getSelectedVideo = () => {
      return videoDeviceSelect.value;
    }
  
    const getSelectedAudio = () => {
      return audioDeviceSelect.value;
    }
    
    let captureStream = MediaStream;
    startButton.addEventListener("click", async () => {
      videoContainer.innerHTML = '';
  
      captureStream = await navigator.mediaDevices.getUserMedia({video: { deviceId: getSelectedVideo()}, audio: {deviceId: getSelectedAudio()}});
      const video = document.createElement("video");
      video.autoplay = true;
      video.srcObject = captureStream;
      video.classList.add("w-100");
      videoContainer.appendChild(video);
    });

    shotButton.addEventListener('click', async () => {
      const videoTrack = captureStream.getVideoTracks()[0];
      const imageCapture = new ImageCapture(videoTrack);
      const imageBitmap = await imageCapture.grabFrame();
      console.log('Grabbed frame:', imageBitmap);
      
      canvasContainer.innerHTML = '';
      const canvas = document.createElement("canvas");
      canvas.width = imageBitmap.width;
      canvas.height = imageBitmap.height;
      canvas.getContext('2d').drawImage(imageBitmap, 0, 0);
      canvasContainer.appendChild(canvas);
      img.src = canvas.toDataURL('image/png');
    });

  
  };
  
  init();

  $("#input_image").on('change', function(){
    console.log("変更");

    const formData = new FormData();
    const fileField = document.querySelector('input[type="file"]');

    formData.append('avatar', fileField.files[0]);
    console.log(formData);
    console.log(fileField);

    $.ajax({
      type: 'POST',       //通信方法 (GET / POST)
      url: '/', //データ渡し先 (Pythonファイル)
      body: formData
    })
    .done(function (array) {
      //通信成功時の処理
      console.log("ajax通信に成功");
      $("#output img").attr('src', response );
    })
    .fail(function (jqXHR, textStatus, errorThrown) {
      // 通信失敗時の処理
      console.log("ajax通信に失敗しまた");
      console.log("jqXHR          : " + jqXHR.status); // HTTPステータスが取得
      console.log("textStatus     : " + textStatus);    // タイムアウト、パースエラー
      console.log("errorThrown    : " + errorThrown.message); // 例外情報
    });
  });

  (function () {
    'use strict';

    var onClickButton = function () {
        var html =
                '<form id="uploadForm" class="upload-form" style="display: none;">' +
                '<input id="theFile" name="the_file" type="file">' +
                '</form>';
        $('body').append(html);
        $('#theFile').on('change', uploadFile).click();
    };

    var uploadFile = function () {
        var formData = new FormData($('#uploadForm')[0]);
        formData.append('other_data', 999);
        $.ajax({
            url: '/',
            type: 'post',
            data: formData,
            processData: false,
            contentType: false,
            timeout: 10000
        }).done(function () {
            console.log('done');
        }).fail(function () {
            console.log('fail');
        }).then(function () {
            $('#uploadForm').remove();
        });

    };

    $('button').on('click', onClickButton);
})();