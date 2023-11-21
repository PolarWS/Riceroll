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
    mounted() {
        this.$nextTick(() => {
            const blocks = document.querySelectorAll('pre code');
            blocks.forEach((block) => {
                block.textContent = this.escapeHTML(block.textContent);
                hljs.highlightElement(block);
            });
        });
    },
    methods: {
        escapeHTML(str) {
            return str.replace(/[&<>'"]/g,
                tag => ({
                    '&': '&amp;',
                    '<': '&lt;',
                    '>': '&gt;',
                    "'": '&#39;',
                    '"': '&quot;'
                }[tag]));
        }
    }
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