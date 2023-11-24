<template>
    <div class="markdown-body ">
        <Markdown :source="this.markDownData" />
    </div>
</template>

<script>
import Markdown from 'vue3-markdown-it';
import hljs from 'highlight.js';
import 'highlight.js/styles/github.css';
import '../assets/github-markdown.css';

export default {
    components: {
        Markdown
    },
    props: {
        markDownData: String,
    },
    updated() {
        this.$nextTick(() => {
            const blocks = document.querySelectorAll('pre code');
            blocks.forEach((block) => {
                const result = hljs.highlightAuto(block.textContent);
                block.innerHTML = result.value;
            });
        });
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