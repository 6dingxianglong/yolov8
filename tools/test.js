const onFileChange = async (event) => {
    pic.value=[];
    identifyStore.removeState();
    if (authStore.username === '') {
      alertStore.callAlert("請先登入才能使用", '注意', 'error');
      return;
    }
    if (file.value === null) {
      alertStore.callAlert("沒有選擇任何圖片", '注意', 'error');
      return;
    }
    const reader = new FileReader();
    await reader.readAsDataURL(file.value); // 讀取文件並觸發 onload 事件
    reader.onload = async function (event) {
      const base64Image = reader.result; // 將圖片轉換成 Base64 字串
      // 確保 uploadImageBase64 完成後再執行 getIdentifyImg
      try {
        await identifyStore.uploadImageBase64(createBase64Json(base64Image));
        await console.log(createBase64Json(base64Image));
        await identifyStore.getIdentifyImg(createJson());
        await console.log(createJson());
        const result = await identifyStore.getImg(identifyStore.image_filenames[0]);
        for (let i = 0; i < identifyStore.image_filenames.length; i++) {
          const result = await identifyStore.getImg(identifyStore.image_filenames[i]);
          pic.value[i] = result.imageUrl; // 使用 value 屬性設置值
        }
        file.value = null;
      } catch (error) {
        console.error(error);
        // 在這裡處理錯誤
      }
    };
  }