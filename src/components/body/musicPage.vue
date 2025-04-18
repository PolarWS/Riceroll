<template>
    <bodyItem :itemData="this.itemData"></bodyItem>
</template>
<script>
import bodyItem from '@/components/body/bodyItem.vue';
export default {
    components: {
        bodyItem,
    }, props: {
        itemData: Object,
    },
}
</script>