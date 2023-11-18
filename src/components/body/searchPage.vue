<template>
    <bodyItem :itemData="this.itemData"/>
</template>
<script>
import bodyItem from './bodyItem.vue';
export default{
    components:{
        bodyItem,
    },props:{
        itemData:Object,
    }
}
</script>