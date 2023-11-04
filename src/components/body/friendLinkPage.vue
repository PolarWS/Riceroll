<template>
    <div class="card_box" v-for="(card,index) in cardList">
        <img class="card_img" :src= "(card.src)"/>
        <div class="card-content">
          <h2 class="title">{{ card.title }}</h2>
          <p class="content">{{ card.content }}</p>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return{
            cardList:[
                {
                    src:"/src/components/img/zhuye.png",
                    title:"只是标题1",
                    content:"看什么看，内容没见过啊！"
                },
                {
                    src:"/src/components/img/zhuye.png",
                    title:"2号标题",
                    content:"看什么看，内容没见过啊！是不是没见过！是不是没见过！是不是没见过！是不是没见过！"
                },
                {
                    src:"/src/components/img/zhuye.png",
                    title:"怎么看也就只是标题啊",
                    content:"看什么看，内容没见过啊！"
                }
            ]
        }
    }
}
</script>
<style>
    .card_box{
        margin: 20px;
        width: 50%;
        height: 150px;
        display: flex;
        justify-content: space-between;
        border: 2px solid red;
        background-color: #F4F4F4;
        border-radius: 15px;
    }
    .card_img{
        margin: auto auto;
        height: 100px;
        width: 100px;
        border-radius: 50px;
    }
    .card_content{
        flex: 1;
        margin-left: 10px
    }
    .title{
        width: 200px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .content{
        height: 45px;
        width: 200px;
        word-break: break-all;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
</style>