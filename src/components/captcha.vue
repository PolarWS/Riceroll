<template>
    <div class="captcha">
        <loadingDynamicEffect v-show="loadingDisplay" />
        <div class="captchaImg" v-show="!loadingDisplay"
            :style="`background-image: url(${this.img}); transform: rotate(${-this.angle}deg); transition: ${isDragging ? 'none' : 'transform 0.5s ease-out'};`">
            <div v-if="rotatingAnimation">
                <lord-icon v-pre src="https://cdn.lordicon.com/rsbokaso.json" trigger="in" delay="300"
                    state="in-autorenew" colors="primary:#ffffff" style="width:5rem;height:5rem">
                </lord-icon>
            </div>
            <div v-if="!rotatingAnimation && !verify">
                <lord-icon v-pre src="https://cdn.lordicon.com/nqtddedc.json" trigger="in" delay="100" state="in-cross"
                    colors="primary:#ffffff" style="width:5rem;height:5rem">
                </lord-icon>
            </div>
            <div v-if="!rotatingAnimation && verify">
                <lord-icon v-pre src="https://cdn.lordicon.com/oqdmuxru.json" trigger="in" delay="100" state="in-check"
                    colors="primary:#ffffff" style="width:5rem;height:5rem">
                </lord-icon>
            </div>
        </div>
        <div class="captchaSliderBox">
            <div class="captchaSlider" v-show="!loadingDisplay">
                <div class="sliderButtom"
                    :style="{ 'margin-left': `${marginLeft}px`, 'transition': isDragging && !requestLoading ? 'none' : 'margin-left 0.5s ease-out' }"
                    @mousedown="handleMouseDown" @mousemove="handleMouseMove" @mouseup="handleMouseUp"
                    @mouseleave="handleMouseLeave" @touchstart="handleTouchDown" @touchmove="handleTouchMove"
                    @touchend="handleMouseUp" @touchcancel="handleMouseLeave">
                    <svg t="1713365239894" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="1894" width="17" height="17">
                        <path
                            d="M405.3 64v896L832 521.2 405.3 64zM234.7 191.6c-23.6 0-42.7 19.1-42.7 42.7V789c0 23.6 19.1 42.7 42.7 42.7s42.7-19.1 42.7-42.7V234.2c-0.1-23.5-19.2-42.6-42.7-42.6z"
                            fill="#F3F3F3" p-id="1895"></path>
                    </svg>
                </div>
                <div class="sliderTxt">
                    改平图片
                </div>
            </div>
            <div class="closeSlider" @click="closeClick" v-show="!loadingDisplay">
                <svg t="1719942100697" class="icon" viewBox="0 0 1025 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="4269" width="11" height="11">
                    <path
                        d="M997.553471 154.252491 639.804427 512.001535 997.553471 869.751602l0 0c16.34988 16.374439 26.450623 38.948897 26.450623 63.898376 0 49.899981-40.450041 90.350022-90.351045 90.350022-24.949479 0-47.549519-10.100743-63.897353-26.475181l0 0L512.003581 639.775775 154.255561 997.525842l0 0c-16.34988 16.374439-38.948897 26.475181-63.899399 26.475181-49.901004 0-90.350022-40.450041-90.350022-90.350022 0-24.950502 10.099719-47.523938 26.449599-63.898376l0 0 357.750067-357.750067L26.454716 154.252491l0 0c-16.34988-16.350903-26.449599-38.949921-26.449599-63.900423 0-49.899981 40.449018-90.348999 90.350022-90.348999 24.950502 0 47.550543 10.099719 63.899399 26.474158l0 0 357.748021 357.749044L869.754672 26.477228l0 0c16.348857-16.374439 38.948897-26.474158 63.897353-26.474158 49.901004 0 90.351045 40.449018 90.351045 90.348999C1024.00307 115.301547 1013.902327 137.901588 997.553471 154.252491L997.553471 154.252491z"
                        p-id="4270" fill="#ffffff"></path>
                </svg>
            </div>
        </div>
    </div>
</template>
<script>
import lottie from "lottie-web";
import { defineElement } from "@lordicon/element";
import { axiosStore } from '@/store/axiosStore.js';
import loadingDynamicEffect from '@/components/loadingDynamicEffect.vue';
defineElement(lottie.loadAnimation);
export default {
    data() {
        return {
            api: axiosStore().api,
            loadingDisplay: true,
            requestLoading: false,
            isDragging: false,
            rotatingAnimation: true,
            verify: false,
            Position: 0,
            angle: 0,
            marginLeft: 4,
            img: String,
            id: Number,
            mouseData: [],
        };
    },
    methods: {
        handleTouchDown(event) {
            event.preventDefault();
            if (this.requestLoading) return;
            this.Position = event.touches[0].clientX;
            this.isDragging = true;
            this.rotatingAnimation = true;
            this.mouseData = [];
        },
        handleTouchMove(event) {
            event.preventDefault();
            if (this.isDragging) {
                this.marginLeft = Math.max(4, Math.min(146, 4 + event.touches[0].clientX - this.Position));
                this.angle = (this.marginLeft - 4) / (146 - 4) * (360 - 0) + 0;
                this.mouseData.push([event.touches[0].clientY, event.touches[0].clientX, Date.now()]);
            }
        },
        handleMouseDown(event) {
            if (this.requestLoading) return;
            this.Position = event.clientX;
            this.isDragging = true;
            this.rotatingAnimation = true;
            this.mouseData = [];
        },
        handleMouseMove(event) {
            if (this.isDragging) {
                this.marginLeft = Math.max(4, Math.min(146, 4 + event.clientX - this.Position));
                this.angle = (this.marginLeft - 4) / (146 - 4) * (360 - 0) + 0;
                this.mouseData.push([event.clientY, event.clientX, Date.now()]);
            }
        },
        handleMouseLeave() {
            if (this.isDragging) this.handleMouseUp();
        },
        handleMouseUp(event) {
            this.requestLoading = true;
            axiosStore().apiRequest(this.api.url + this.api.captcha.captchaCheck, {
                id: this.id,
                rotation: 360 - this.angle,
                mouseData: this.mouseData.slice(0, 300),
            }, "post")
                .then(data => {
                    if (data.status == 200) {
                        this.marginLeft = 4;
                        this.angle = 0;
                        this.verify = true;
                        this.rotatingAnimation = false;
                        this.requestLoading = false;
                        this.$emit('passID', data.data.value);
                    } else {
                        this.marginLeft = 4;
                        this.angle = 0;
                        this.verify = false;
                        this.rotatingAnimation = false;
                        this.loadingImg();
                        this.requestLoading = false;
                    }
                })
            this.isDragging = false;
        }, closeClick() {
            this.$emit('close');
        }, loadingImg() {
            axiosStore().apiRequest(this.api.url + this.api.captcha.captchaCreate, {}, "post")
                .then(data => {
                    if (data.status == 200) {
                        this.id = data.data.value;
                        this.img = this.api.url + this.api.captcha.captchaImage + '?id=' + this.id;
                        this.loadingDisplay = false;
                    }
                })
        }
    }, components: {
        loadingDynamicEffect,
    }, mounted() {
        this.loadingImg();
    }
}
</script>
<style>
.captcha {
    width: 100%;
    min-height: 15rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.captchaSliderBox {
    display: flex;
    height: 3rem;
}

.closeSlider {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 1rem;
    width: 2.5rem;
    background-color: var(--color-theme-R);
    border-radius: 0.75rem;
    cursor: pointer;
}

.captchaSlider {
    display: flex;
    align-items: center;
    width: 11rem;
    height: 100%;
    background-color: var(--color-theme-grayscale1);
    border-radius: 0.75rem;
}

.captchaImg {
    width: 10rem;
    height: 10rem;
    margin: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background-size: cover;
    background-position: center;
    transition: transform 0.5s ease-out;
}

.sliderButtom {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 0.65rem;
    margin-left: 0.25rem;
    cursor: pointer;
    background-color: var(--color-theme-white);
    transition: margin-left 0.15s cubic-bezier(0, 0, .58, 1);
}

.sliderButtom:active {
    background-color: var(--color-theme-grayscale3);
}

.sliderTxt {
    user-select: none;
    color: var(--color-theme-grayscale4);
    font-size: 0.9rem;
    letter-spacing: 0.5rem;
    margin-left: 3.5rem;
}
</style>