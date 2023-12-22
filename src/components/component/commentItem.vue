<template>
    <div class="commentItemInfo">
        <div class="commentitemBasicInfo">
            <div class="commentItemInfoImg" v-if="!commentItemInfoReplyImgDisplay"
                :style="{ backgroundImage: `url(${commentItemData.avatarImg})` }">
            </div>
            <div class="commentItemInfoReplyImg" v-if="commentItemInfoReplyImgDisplay"
                :style="{ backgroundImage: `url(${commentItemData.avatarImg})` }">
            </div>
            <div class="commentItemInfoND">
                <div class="commentItemInfoName" @click="urlRedirect(commentItemData.url)">
                    {{ commentItemData.name }}
                </div>
                <div class="commentItemInfoDate">
                    {{ commentItemData.date }}
                </div>
                <div class="commentItemMsg" v-html="commentItemData.msg">
                </div>
            </div>
        </div>
        <div class="commentItemReply">
            <button @click="commentSectionDisplay()">
                <svg t="1703078259309" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="4558" width="20" height="20">
                    <path
                        d="M185.2 888.7c-16.6 0-30-13.4-30-30v-580c0-49.6 40.4-90 90-90h540c49.6 0 90 40.4 90 90v410c0 49.6-40.4 90-90 90h-429c-16.6 0-30-13.4-30-30s13.4-30 30-30h429c16.5 0 30-13.5 30-30v-410c0-16.5-13.5-30-30-30h-540c-16.5 0-30 13.5-30 30v580c0 16.5-13.5 30-30 30z m490.1-430.5H347c-16.6 0-30-13.4-30-30s13.4-30 30-30h328.3c16.6 0 30 13.4 30 30s-13.4 30-30 30zM494 598.2H345.7c-16.6 0-30-13.4-30-30s13.4-30 30-30H494c16.6 0 30 13.4 30 30s-13.4 30-30 30zM194.2 883.7c-9.8 0-19.3-4.8-25.1-13.5-9.1-13.9-5.2-32.5 8.6-41.5l160-105c13.9-9.1 32.5-5.2 41.5 8.6 9.1 13.9 5.2 32.5-8.6 41.5l-160 105c-5 3.3-10.8 4.9-16.4 4.9z"
                        fill="#2c2c2c" p-id="4559"></path>
                </svg>
            </button>
        </div>
    </div>
    <div class="commentSectionBox" ref="commentSectionBox">
        <transition name="slide" @enter="enter" @leave="leave">
            <commentSection ref="commentSection" v-show="commentItemData.commentSectionDisplay"
                :linkName="'@' + commentItemData.name" />
        </transition>
    </div>
</template>
<script>
import commentSection from './commentSection.vue';
export default {
    methods: {
        urlRedirect(url) {
            window.open(url);
        }, updateHeight() {
            const el = this.$refs.commentSectionBox.children[0];
            const style = window.getComputedStyle(el);
            const marginTop = parseFloat(style.marginTop);
            const marginBottom = parseFloat(style.marginBottom);
            this.$refs.commentSectionBox.style.height = el.scrollHeight + marginTop + marginBottom + 'px';
        }, enter(el, done) {
            this.$refs.commentSectionBox.style.height = '0';
            setTimeout(() => {
                this.updateHeight();
            }, 0);
            done();
        }, leave(el, done) {
            this.updateHeight();
            setTimeout(() => {
                this.$refs.commentSectionBox.style.height = '0';
            }, 0);
            done();
        }, commentSectionDisplay() {
            this.$emit('commentSectionDisplay', this.commentItemData.uuid);
        }
    }, mounted() {
        window.addEventListener('resize', this.updateHeight);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.updateHeight);
    }, components: {
        commentSection
    }, props: {
        commentItemData: Object,
        commentItemInfoReplyImgDisplay: {
            type: Boolean,
            default: () => (false)
        }
    }, emits: ['commentSectionDisplay'],
}
</script>
<style>
.commentItemInfo {
    margin-bottom: 1.25rem;
    display: flex;
    justify-content: space-between;

}

.commentItemInfoImg {
    width: 5.75rem;
    height: 5.75rem;
}

.commentItemInfoReplyImg {
    width: 4.5rem;
    height: 4.5rem;
}

.commentItemInfoImg,
.commentItemInfoReplyImg {
    border-radius: 50%;
    background-size: 100%;
    background-position: center;
    background-repeat: no-repeat;
    transition: background-size 0.3s;
}

.commentItemInfoImg:hover,
.commentItemInfoReplyImg:hover {
    background-size: 110%
}

.commentitemBasicInfo {
    display: grid;
    grid-template-columns: 5.75rem 1fr;
}

.commentItemInfoND {
    padding: 0.75rem 0 0 1.25rem;
}

.commentItemInfoName {
    display: inline-block;
    word-break: break-all;
    font-size: 1.35rem;
    font-weight: 600;
    cursor: pointer;
    transition: color 0.1s;
}

.commentItemInfoName:hover {
    color: var(--color-theme-blue-1);
}

.commentItemInfoDate {
    word-break: break-all;
    margin-top: 0.25rem;
    color: var(--color-theme-grayscale6);
}

.commentItemMsg {
    word-break: break-all;
    margin-top: 1.25rem;
}

.commentItemReply {
    padding-top: 2rem;
}

.commentItemReply button {
    padding: 0.2rem;
    height: 2.25rem;
    width: 2.25rem;
    border-radius: 50%;
    border: 0px;
    background-color: var(--color-theme-white);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.15s;
    font-size: 1.15rem;
}

.commentItemReply button:hover {
    background-color: var(--color-theme-grayscale1);
}

.commentItemReply button:active {
    background-color: var(--color-theme-grayscale3);
}

.commentSectionBox {
    overflow: hidden;
    transition: height .3s ease;
}

@media screen and (max-width: 600px) {
    .commentitemBasicInfo {
        grid-template-columns: 4.5rem 1fr;
    }

    .commentItemInfoImg {
        width: 4.5rem;
        height: 4.5rem;
    }

    .commentItemInfoReplyImg {
        width: 3.75rem;
        height: 3.75rem;
    }
}
</style>