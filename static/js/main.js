var showData = document.getElementsByClassName('showProd')

for(var i =0; i<showData.length;i++){
    showData[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product:', productId,'action:', action)

        showItem(productId, action)
    })
}

function showItem(productId, action){

    console.log('log')

    var url = '/showItem/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'applicaiton/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json();
    })

    .then((data) =>{
        console.log('data', data)
    })

}

var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder='Username..';
form_fields[2].placeholder='Email..';
form_fields[3].placeholder='Enter password...';
form_fields[4].placeholder='Re-enter Password...';


for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}