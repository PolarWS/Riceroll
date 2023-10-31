<template>
    <div class="topImg">
        <img :src="topimg.src" :alt="topimg.alt">
    </div>
    <div class="avatarImg">
        <img :src="avatar.src" :alt="avatar.alt">
    </div>
</template>
<script>
export default {
    data() {
        return {
            topimg: {
                src: "/src/components/img/zhuye.png",
                alt: "topimg",
            },
            avatar: {
                src: "/src/components/img/avatar.jpg",
                alt: "avatar",
            }
        }
    },
}
</script>
<style>
.topImg {
    width: 100%;
    height: 20rem;
}

.avatarImg {
    margin-top: -5rem;
    display: flex;
}

.avatarImg img {
    width: 10rem;
    height: 10rem;
    margin-left: 2rem;
    border-radius: 50%;
    border: 0.35rem solid #fff;
}

img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>