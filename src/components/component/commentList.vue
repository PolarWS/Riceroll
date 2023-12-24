<template>
    <div class="commentList" v-if="this.commentListDisplay">
        <commentSection :commentDataUpdate="commentDataUpdate" />
        <div class="commentListBox" v-for="(item, index) in commentData" :id="item.uuid" :key="item.uuid">
            <commentItem :commentItemData="item" @commentSectionDisplay="commentSectionDisplay"
                :commentDataUpdateBranch="commentDataUpdateBranch" />
            <div class="commentListReplyBox" v-for="(item, index) in item.reply" :id="item.uuid" :key="item.uuid">
                <commentItem :commentItemData="item" :commentItemInfoReplyImgDisplay=true
                    @commentSectionDisplay="commentSectionDisplay" :commentDataUpdateBranch="commentDataUpdateBranch" />
            </div>
        </div>
    </div>
    <loadingDynamicEffect v-else />
</template>
<script>
import commentItem from './commentItem.vue';
import commentSection from './commentSection.vue';
import loadingDynamicEffect from '../loadingDynamicEffect.vue';
import { useCounterStore } from '../../store/axiosStore.js';
export default {
    data() {
        return {
            commentData: Object,
            commentListDisplay: false,
        }
    },
    created() {
        useCounterStore().apiRequest(this.api.url + this.api.comment[0], { "route": this.$route.path.split('/').pop() })
            .then(data => {
                if (data.status == 200) {
                    this.commentData = data.data;
                    this.commentData = this.commentData.map(item => ({
                        ...item,
                        commentSectionDisplay: false,
                        reply: item.reply.map(replyItem => ({
                            ...replyItem,
                            commentSectionDisplay: false,
                        }))
                    }));
                    this.commentListDisplay = true;
                } else if (data.status == 400) {
                    this.$root.messagePopups({
                        message: data.news,
                        Color: 'messageR',
                    });
                }
            });
    }, methods: {
        commentDataUpdate(commentDataAdd) {
            this.commentData = [commentDataAdd, ...this.commentData];
        },
        commentDataUpdateBranch(commentDataAdd) {
            for (let i = 0; i < this.commentData.length; i++) {
                if (this.commentData[i].uuid === commentDataAdd.uuidLink) {
                    this.commentData[i].reply.splice(0, 0, commentDataAdd);
                    this.commentSectionDisplay(commentDataAdd.uuidLink)
                    return;
                }
                for (let j = 0; j < this.commentData[i].reply.length; j++) {
                    if (this.commentData[i].reply[j].uuid === commentDataAdd.uuidLink) {
                        this.commentData[i].reply.splice(j + 1, 0, commentDataAdd);
                        this.commentSectionDisplay(commentDataAdd.uuidLink)
                        return;
                    }
                }
            }
        },
        commentSectionDisplay(uuid) {
            this.commentData = this.commentData.map(item => ({
                ...item,
                commentSectionDisplay: item.uuid === uuid ? !item.commentSectionDisplay : false,
                reply: item.reply.map(replyItem => ({
                    ...replyItem,
                    commentSectionDisplay: replyItem.uuid === uuid ? !replyItem.commentSectionDisplay : false,
                }))
            }));
        },
    },
    components: {
        commentItem,
        commentSection,
        loadingDynamicEffect,
    }, inject: ['api'],
}
</script>
<style scoped>
.commentList {
    padding: 0 1.5rem 0 1.5rem;
}

.commentListBox {
    padding: 1.75rem 1rem 0.5rem 1rem;
    border-top: 1px solid var(--color-theme-frame2);
}

.commentListReplyBox {
    padding-left: 0.5rem;
}

@media screen and (max-width: 600px) {
    .commentList {
        padding: 0 1rem 1rem 1rem;
    }

    .commentListBox {
        padding: 1.75rem 0.75rem 0.25rem 0.75rem;
    }

    .commentListReplyBox {
        padding-left: 0.5rem;
    }
}
</style>