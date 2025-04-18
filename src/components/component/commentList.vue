<template>
    <div class="commentList" v-if="commentListDisplay">
        <commentSection :commentDataUpdate="commentDataUpdate" v-if="commentLock" />
        <div class="commentListBox" v-for="item in filteredComments" :id="item.uuid" :key="item.uuid">
            <commentItem :commentItemData="item" :commentLock="commentLock"
                @commentSectionDisplay="commentSectionDisplay" :commentDataUpdateBranch="commentDataUpdateBranch" />
            <div class="commentListReplyBox"
                v-for="comment in commentData.filter(comment => comment.rid == item.rid && comment.uuid != item.rid)"
                :id="comment.uuid" :key="comment.uuid">
                <commentItem :commentItemData="comment" :commentLock="commentLock" :commentItemInfoReplyImgDisplay=true
                    @commentSectionDisplay="commentSectionDisplay" :commentDataUpdateBranch="commentDataUpdateBranch" />
            </div>
        </div>
        <div class="loadRequestBox" v-if="page < pageMax">
            <div class="loadRequestBut">
                <span v-if="loadRequestButDisplay" @click="addComments">加载更多</span>
                <loadingDynamicEffect v-else :loadingSize="{ size: 25 }" />
            </div>
        </div>
    </div>
    <loadingDynamicEffect v-else />
</template>
<script>
import commentItem from '@/components/component/commentItem.vue';
import commentSection from '@/components/component/commentSection.vue';
import loadingDynamicEffect from '@/components/loadingDynamicEffect.vue';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            api: axiosStore().api,
            commentData: Object,
            commentListDisplay: false,
            loadRequestButDisplay: true,
            page: 1,
            pageMax: 1,
            apc: "",
        }
    },
    props: {
        commentLock: {
            type: Number,
            default: 1,
        }
    },
    created() {
        if (/^[a-f0-9]{32}$/.test(this.$route.fullPath.split('/').pop().split('#')[1])) {
            this.apc = this.$route.fullPath.split('/').pop().split('#')[1];
        }
        axiosStore().apiRequest(this.api.url + this.api.comment.commentList, { "url": this.$route.path, "page": this.page, "apc": this.apc }, "get")
            .then(data => {
                if (data.status == 200) {
                    this.commentData = data.data;
                    this.pageMax = data.pages;
                    this.commentData = data.data.map(item => ({
                        ...item,
                        commentSectionDisplay: false,
                    }));
                    this.commentListDisplay = true;
                }
            });
    }, computed: {
        filteredComments() {
            return this.commentData.filter(comment => comment.pid == "");
        },
    }, methods: {
        addComments() {
            this.page++;
            this.loadRequestButDisplay = false;
            axiosStore().apiRequest(this.api.url + this.api.comment.commentList, { "url": this.$route.path, "page": this.page, "apc": this.apc }, "get")
                .then(data => {
                    if (data.status == 200) {
                        this.commentData = [...this.commentData, ...data.data];
                        this.commentData = this.commentData.map(item => ({
                            ...item,
                            commentSectionDisplay: false,
                        }));
                        this.pageMax = data.pages;
                        this.loadRequestButDisplay = true;
                    }
                });
        },
        commentDataUpdate(commentDataAdd) {
            this.commentData = [commentDataAdd, ...this.commentData];
        },
        commentDataUpdateBranch(commentDataAdd) {
            if (commentDataAdd.pid != "") {
                this.commentSectionDisplay(commentDataAdd.pid);
            }
            for (let i = 0; i < this.commentData.length; i++) {
                if (this.commentData[i].uuid === commentDataAdd.pid) {
                    this.commentData.splice(i + 1, 0, commentDataAdd);
                    return;
                }
            }
            this.commentData.unshift(commentDataAdd);
        },
        commentSectionDisplay(uuid) {
            this.commentData = this.commentData.map(item => ({
                ...item,
                commentSectionDisplay: item.uuid === uuid ? !item.commentSectionDisplay : false,
            }));
        },
    },
    components: {
        commentItem,
        commentSection,
        loadingDynamicEffect,
    },
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

.loadRequestBox {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
}

.loadRequestBut {
    background-color: var(--color-theme-grayscale2);
    color: var(--color-theme-grayscale65);
    width: 7rem;
    height: 2.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    user-select: none;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
}

.loadRequestBut:active {
    background-color: var(--color-theme-grayscale3);
    color: var(--color-theme-grayscale6);
}

/* .commentListReplyBox {
    padding-left: 0.5rem;
} */

@media screen and (max-width: 600px) {
    .commentList {
        padding: 0 1rem 1rem 1rem;
    }

    .commentListBox {
        padding: 1.75rem 0.75rem 0.25rem 0.75rem;
    }

    /* .commentListReplyBox {
        padding-left: 0.5rem;
    } */
}
</style>