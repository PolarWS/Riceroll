<template>
    <div v-show="renderBoolean" class="pageMD">
        <div id="bodyItemTopImg" :style="`background-image: url(${this.api.url + this.api.cover + '/' + markDownData.title.cover})`">
            <div class="brightnessAdjustment">
                <div id="bodyItemTopTitle">
                    <h1>「{{ markDownData.title.content }}」</h1>
                </div>
                <div id="bodyItemTopSpanBox">
                    <div class="bodyItemTopSpan">
                        <svg t="1700204012481" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="11426" width="15" height="15">
                            <path
                                d="M739.196 198c-7.092 14.786-22.202 24.996-39.696 24.996-17.494 0-32.604-10.21-39.696-24.996H351.196c-7.092 14.786-22.202 24.996-39.696 24.996-17.494 0-32.604-10.21-39.696-24.996H133c-24.3 0-44 19.7-44 44v109.64a44.123 44.123 0 0 1 10.179-1.14L933 353.89V242c0-24.3-19.7-44-44-44H739.196z m4.304-88H889c72.902 0 132 59.098 132 132v594c0 72.902-59.098 132-132 132H133C60.098 968 1 908.902 1 836V242c0-72.902 59.098-132 132-132h134.5V45c0-24.3 19.7-44 44-44s44 19.7 44 44v65h300V45c0-24.3 19.7-44 44-44s44 19.7 44 44v65zM89 437.358V836c0 24.3 19.7 44 44 44h756c24.3 0 44-19.7 44-44V441.891L98.821 438.5A44.142 44.142 0 0 1 89 437.358zM274 721.5c-24.3 0-44-19.7-44-44s19.7-44 44-44h471.114c24.3 0 44 19.7 44 44s-19.7 44-44 44H274z"
                                fill="#ffffff" p-id="11427"></path>
                        </svg>
                        <span>{{ markDownData.date.slice(0, 10) }}</span>
                    </div>
                    <div class="bodyItemTopSpan">
                        <svg t="1700205663159" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="2420" width="18" height="18">
                            <path
                                d="M896 128a42.7 42.7 0 0 1 42.7 42.7v682.7a42.7 42.7 0 0 1-42.7 42.7H128a42.7 42.7 0 0 1-42.7-42.7V170.7A42.7 42.7 0 0 1 128 128h768z m-42.7 85.3H170.7v597.3h682.7V213.3zM401 341.3l136.5 341.3h-91.9l-17.1-42.7H288.1L271 682.6h-91.8l136.5-341.3H401z m409.7 0v341.3h-128a128 128 0 0 1 0-256h42.6v-85.3h85.3zM725.4 512h-42.7a42.7 42.7 0 0 0-5 85l5 0.3h42.7V512z m-367-47.6l-36.2 90.3h72.2l-36.1-90.2z"
                                p-id="2421" fill="#ffffff"></path>
                        </svg>
                        <span>{{ markDownData.wordCount }}</span>
                    </div>
                </div>
            </div>
        </div>
        <markDown :markDownData="markDownData.md" />
        <tagPanel :tagData="markDownData.tag" v-show="renderBoolean" class="pageMD" />
        <commentList :commentLock="markDownData.commentRead" />
    </div>
    <loadingDynamicEffect v-show="!renderBoolean" />
</template>
<script>
import markDown from '@/components/markDown.vue';
import commentList from '@/components/component/commentList.vue';
import tagPanel from '@/components/tagPanel.vue';
import loadingDynamicEffect from '@/components/loadingDynamicEffect.vue';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            api: axiosStore().api,
            renderBoolean: false,
            markdownTocIndex: -1,
            markDownData: {
                "title": {
                    "content": "",
                    "cover": ""
                },
                "md": "",
                "date": "",
                "wordCount": "",
                "commentRead": 1,
                "tag": []
            },
            markdownID: String,
            completeRenderingRequest: false,
        }
    },
    watch: {
        markdownTocIndex(newVal) {
            this.$root.markdownTocIndexs(newVal - 1);
        },
    },
    mounted() {
        this.markdownID = this.$route.path.split('/');
        axiosStore().apiRequest(this.api.url + this.api.markdown,
            { "id": this.markdownID[this.markdownID.length - 1] }, "get")
            .then(data => {
                if (data.status == 200) {
                    this.markDownData = data.data;
                    if (data.data.toc.length < 1) {
                        this.$root.markdownToc({
                            display: true,
                            data: data.data.toc,
                        })
                    }
                    this.renderBoolean = true;
                    const routeName = this.$route.fullPath.split('/').pop();
                    if (routeName.split('#').length > 1) {
                        const anchor = routeName.split('#')[1];
                        setTimeout(() => {
                            const anchorElement = document.getElementById(anchor);
                            if (anchorElement) {
                                anchorElement.scrollIntoView({ behavior: 'smooth' });
                            }
                            setTimeout(() => {
                                this.completeRenderingRequest = true;
                                this.checkAnchorInViewport();
                            }, 550);
                        }, 1000);
                    } else {
                        this.completeRenderingRequest = true;
                        this.checkAnchorInViewport();
                    }
                }
            })
        window.addEventListener('scroll', this.checkAnchorInViewport, false);
    }, methods: {
        checkAnchorInViewport() {
            if (this.completeRenderingRequest) {
                const anchors = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6'));
                const newAnchorIndex = anchors.findIndex(anchor => {
                    const rect = anchor.getBoundingClientRect();
                    return rect.top >= 0 && rect.bottom <= window.innerHeight;
                });
                if (newAnchorIndex !== this.markdownTocIndex) {
                    this.markdownTocIndex = newAnchorIndex;
                }
            }
        },
    }, unmounted() {
        this.$root.markdownToc({
            display: false,
            data: '',
        })
        window.removeEventListener('scroll', this.checkAnchorInViewport);
    },
    components: {
        markDown,
        loadingDynamicEffect,
        tagPanel,
        commentList,
    },
}
</script>
<style scoped>
.pageMD {
    animation-name: fadeIn;
    animation-duration: 0.5s;
}

.brightnessAdjustment {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--color-theme-white);
    background-color: var(--color-theme-black0);
}

#bodyItemTopImg {
    width: 100%;
    height: 15rem;
    background-size: 100%;
    background-position: center;
    background-repeat: no-repeat;
    transition: background-size 0.5s;
}

#bodyItemTopImg:hover {
    background-size: 110%;
}

#bodyItemTopTitle h1 {
    margin: 0.5rem 1.5rem;
}

#bodyItemTopSpanBox {
    display: flex;
}

.bodyItemTopSpan {
    display: flex;
    align-items: center;
    margin-right: 0.75rem;
}

.bodyItemTopSpan span {
    margin-left: 0.35rem;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

@media screen and (max-width: 600px) {
    #bodyItemTopImg {
        background-size: cover;
    }

    #bodyItemTopImg:hover {
        background-size: cover;
    }

    #bodyItemTopTitle h1 {
        margin: 0.5rem 1rem;
    }
}
</style>