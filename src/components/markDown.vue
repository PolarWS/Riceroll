<template>
    <div class="markdown-body">
        <Markdown v-if="markdownDisplay && markdownData" :source="markdownData" :html="plugins.html"
            :breaks="plugins.breaks" :linkify="plugins.linkify" />
    </div>
</template>
<script>
import Markdown from 'vue3-markdown-it';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            plugins: {
                "html": true,
                "breaks": true,
                "linkify": true,
            },
            markdownData: '',
            api: axiosStore().api,
            markdownDisplay: false
        }
    },
    components: {
        Markdown
    },
    created() {
        if (this.markDownUrl) {
            axiosStore().apiRequest(this.api.url + this.api.markdownFile,
                {
                    "file": this.markDownUrl
                })
                .then(data => {
                    if (data.status == 200) {
                        this.markdownData = data.data.md;
                        this.markdownDisplay = true;
                    }
                })
        }
    },
    props: {
        markDownData: String,
        markDownUrl: String,
    },
    watch: {
        markDownData(newVal) {
            this.markdownData = newVal;
            this.markdownDisplay = true;
        }
    }
}
</script>
<style scoped>
.markdown-body {
    padding: 1rem 1.5rem 0.5rem 1.5rem;
}

@media screen and (max-width: 600px) {
    .markdown-body {
        padding: 1rem 1rem 0.5rem 1rem;
    }
}
</style>