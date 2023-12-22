<template>
    <commentSection />
    <div class="commentList">
        <div class="commentListBox" v-for="(item, index) in commentData" :id="item.uuid">
            <commentItem :commentItemData="item" @commentSectionDisplay="commentSectionDisplay" />
            <div class="commentListReplyBox" v-for="(item, index) in item.reply" :id="item.uuid">
                <commentItem :commentItemData="item" :commentItemInfoReplyImgDisplay=true
                    @commentSectionDisplay="commentSectionDisplay" />
            </div>
        </div>
    </div>
</template>
<script>
import commentItem from './commentItem.vue';
import commentSection from './commentSection.vue';
import { useCounterStore } from '../../store/axiosStore.js';
export default {
    data() {
        return {
            commentData: Object
        }
    },
    created() {
        useCounterStore().apiRequest(this.api.url + this.api.comment, { "route": this.$route.path })
            .then(data => {
                if (data.status == 200) {
                    console.log();

                    this.commentData = data.data;
                    this.commentData = this.commentData.map(item => ({
                        ...item,
                        commentSectionDisplay: false,
                        reply: item.reply.map(replyItem => ({
                            ...replyItem,
                            commentSectionDisplay: false,
                        }))
                    }));
                }
            });
    }, methods: {
        commentSectionDisplay(uuid) {
            this.commentData = this.commentData.map(item => ({
                ...item,
                commentSectionDisplay: item.uuid === uuid ? !item.commentSectionDisplay : false,
                reply: item.reply.map(replyItem => ({
                    ...replyItem,
                    commentSectionDisplay: replyItem.uuid === uuid ? !replyItem.commentSectionDisplay : false,
                }))
            }));
        }
    },
    components: {
        commentItem,
        commentSection,
    }, inject: ['api'],
}
</script>
<style scoped>
.commentList {
    padding: 0 1rem;
}

.commentListBox {
    padding: 1rem 1.25rem 0 1.25rem;
    border-top: 1px solid var(--color-theme-frame2);
}

.commentListReplyBox {
    padding-left: 1rem;
}

@media screen and (max-width: 600px) {
    .commentListBox {
        padding-left: 0;
    }

    .commentListReplyBox {
        padding-left: 0.5rem;
    }
}
</style>