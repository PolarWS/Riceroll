<template>
    <div class="markdown-body ">
        <Markdown :source="this.markDownData" />
    </div>
</template>

<script>
import Markdown from 'vue3-markdown-it';

export default {
    components: {
        Markdown
    },
    props: {
        markDownData: String,
    },
}
</script>

<style scoped>
.markdown-body {
    padding: 1.5rem;
}

@media screen and (max-width: 600px) {
    .markdown-body {
        padding: 1rem;
    }
}
</style>