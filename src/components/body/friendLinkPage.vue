<template>
    <div class="father_box" id="pressed">
        <div class="card_box" v-for="(card, index) in cardList" :key="index">
            <img class="card_img" :src="(card.src)" />
            <div class="card-content">
                <h3 class="title">{{ card.title }}</h3>
                <p class="content">{{ card.content }}</p>
                <div class="status-bar" :class="{ 'inaccessible': card.inaccessible }"></div>
            </div>
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
                    content:"看什么看，内容没见过啊！",
                    inaccessible:true
                },
                {
                    src:"/src/components/img/zhuye.png",
                    title:"2号标题",
                    content:"看什么看，内容没见过啊！是不是没见过！是不是没见过！是不是没见过！是不是没见过！",
                    inaccessible:false
                },
                {
                    src:"/src/components/img/zhuye.png",
                    title:"怎么看也就只是标题啊",
                    content:"看什么看，内容没见过啊！",
                    inaccessible:false
                },
                {
                    src:"/src/components/img/zhuye.png",
                    title:"怎么看也就只是标题啊对吧对吧",
                    content:"看什么看，内容没见过啊！",
                    inaccessible:false
                },
                {
                    src:"/src/components/img/zhuye.png",
                    title:"怎么看也就只是标题啊对吧对吧",
                    content:"看什么看，内容没见过啊！是不是没见过！是不是没见过！是不是没见过！是不是没见过！！",
                    inaccessible:false
                }
            ]
        }
    }
}
</script>
<style>
    .father_box {
        display: flex;
        flex-wrap: wrap;
    }

    .card_box {
        display: flex;
        flex-wrap: wrap;
        margin: 20px 16px 0px 16px;
        width: 45%;
        height: auto;
        background-color: #F4F4F4;
        border-radius: 15px;
        position: relative; /* Add this to make the status bar relative to the card */
    }

    .card_img {
        margin: auto auto;
        height: 85px;
        width: 85px;
        border-radius: 50px;
    }

    .card-content {
        margin-left: 10px;
    }

    .title {
        max-width: 190px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .content {
        height: 45px;
        width: 200px;
        word-break: break-all;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }

    .status-bar {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 10px;
        background-color: aqua;
        border-bottom-left-radius: 15px; 
        border-bottom-right-radius: 15px; 
    }

    .status-bar.inaccessible {
        background-color: red;
    }
</style>
