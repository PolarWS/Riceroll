<template>
    <div>
        <div class="topImg">
            <img :src="itemData.topImg.img" :alt="itemData.topImg.alt">
        </div>
        <div v-html="itemData.html"></div>
    </div>
</template>
<script>
export default {
    props: {
        itemData: Object,
    }
}
</script>
<style scoped>
img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.topImg {
    width: 100%;
    height: 20rem;
}
</style>