const fotoDefault = '/media/users/user_default_profile.png';
const foto = document.getElementById('id_picture');
const img = document.getElementById('img_actual');


foto.addEventListener('change', e => {

        if(e.target.files[0]){
            const reader = new FileReader();
            reader.onload = function (e){
                img.src = e.target.result;
            }
            reader.readAsDataURL(e.target.files[0])
            //img.src='/static/img/facebook.png'
        }else{
            img.src= fotoDefault;
        }
    console.log(e.target.files);
});

