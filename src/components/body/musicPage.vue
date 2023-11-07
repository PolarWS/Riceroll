<template>
    <h3>musicPage</h3>
    <!-- <textarea id="multiLineInput" rows="4" cols="50" v-model="multiLineText"></textarea>
    <div>
        <Markdown :source="multiLineText" />
    </div> -->
</template>
<script>
import Markdown from 'vue3-markdown-it';

export default {
    components: {
        Markdown
    },
    data() {
        return {
            // multiLineText: '# Hello World!'
        }
    },props: {
        itemData: Object,
    }
}
</script>
<style></style>