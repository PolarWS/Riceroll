<template>
    <div class="card_box">
        <img class="card_img" />
        <div class="card_title"></div>
        <div class="card_content"></div>
    </div>
</template>
<script>
export default {
    data(){
        return{
            cardList:[
                {
                    url:"",
                    title:"",
                    content:""
                }
            ]
        }
    }
}
</script>
<style>
    .card_box{
        width: 50%;
        height: 170px;
        display: flex;
        justify-content: space-between;
        border: 2px solid red;
        background-color: aqua;
        border-radius: 15px;
    }
    .card_img{
        border-radius: 50px;
    }
</style>