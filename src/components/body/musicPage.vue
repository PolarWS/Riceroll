<template>
    <h3>markDown Test</h3>
    <textarea id="multiLineInput" rows="4" cols="50" v-model="multiLineText"></textarea>
    <div class="markdown-body ">
        <Markdown :source="multiLineText" />
    </div>
</template>

<script>
import Markdown from 'vue3-markdown-it';
import hljs from 'highlight.js';
// import '../../themes/light/mweb-contrast.css';
import 'highlight.js/styles/github.css';
import '../../assets/github-markdown.css';

export default {
    components: {
        Markdown
    },
    data() {
        return {
            multiLineText: '# Hello World!'
        }
    },
    props: {
        itemData: Object,
    },
    mounted() {
        this.$nextTick(() => {
            const blocks = document.querySelectorAll('pre code');
            blocks.forEach((block) => {
                hljs.highlightBlock(block);
            });
        });
    }
}
</script>
<style scoped>
.markdown-body {
    padding: 1.5rem;
}
</style>