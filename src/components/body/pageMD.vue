<template>
    <div v-if="renderBoolean" class="pageMD">
        <div id="bodyItemTopImg" :style="`background-image: url(${markDownData.title.img})`">
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
                        <span>{{ markDownData.date }}</span>
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
    </div>
    <loadingDynamicEffect v-show="!renderBoolean" />
</template>
<script>
import markDown from '../markDown.vue';
import loadingDynamicEffect from '../loadingDynamicEffect.vue';
import { useCounterStore } from '../../store/axiosStore.js';
export default {
    data() {
        return {
            renderBoolean: false,
            markDownData: {},
        }
    }, mounted() {
        const markdownID = this.$route.path.split('/');
        useCounterStore().apiRequest(this.api.url + this.api.markdown + markdownID[markdownID.length - 1]).then(data => {
            this.markDownData = data;
            this.renderBoolean = true;
        });
    }, components: {
        markDown,
        loadingDynamicEffect,
    }, inject: ['api'],
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