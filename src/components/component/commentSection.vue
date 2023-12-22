<template>
   <div class="commentSection">
      <div class="informationSection">
         <div><input type="text" placeholder="昵称"></div>
         <div><input type="text" placeholder="网站"></div>
         <div><input type="text" placeholder="邮箱"></div>
      </div>
      <div class="inputSection">
         <transition name="fade">
            <div class="emojiList" v-show="emojiListVisible">
               😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍
            </div>
         </transition>
         <textarea :placeholder="this.linkName" v-model="textareaValue"></textarea>
      </div>
      <div class="controlArea">
         <div class="controlAreaEmoji">
            <button @click="emojiListVisible = !emojiListVisible">
               <svg t="1702548244505" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                  p-id="6442" width="20" height="20">
                  <path
                     d="M511.5 958.9c-60.3 0-118.9-11.8-174-35.1-53.2-22.5-101-54.7-142.1-95.8-41-41-73.3-88.8-95.8-142.1-23.3-55.1-35.1-113.7-35.1-174s11.8-118.9 35.1-174c22.5-53.2 54.7-101 95.8-142.1 41-41 88.8-73.3 142.1-95.8 55.1-23.3 113.7-35.1 174-35.1s118.9 11.8 174 35.1c53.2 22.5 101 54.7 142.1 95.8 41 41 73.3 88.8 95.8 142.1 23.3 55.1 35.1 113.7 35.1 174s-11.8 118.9-35.1 174c-22.5 53.2-54.7 101-95.8 142.1-41 41-88.8 73.3-142.1 95.8-55.1 23.3-113.6 35.1-174 35.1z m0-838c-52.8 0-104 10.3-152.2 30.7-46.6 19.7-88.4 47.9-124.3 83.8s-64.1 77.7-83.8 124.3c-20.4 48.2-30.7 99.4-30.7 152.2s10.3 104 30.7 152.2c19.7 46.6 47.9 88.4 83.8 124.3s77.7 64.1 124.3 83.8c48.2 20.4 99.4 30.7 152.2 30.7s104-10.3 152.2-30.7c46.6-19.7 88.4-47.9 124.3-83.8 35.9-35.9 64.1-77.7 83.8-124.3 20.4-48.2 30.7-99.4 30.7-152.2s-10.3-104-30.7-152.2c-19.7-46.6-47.9-88.4-83.8-124.3-35.9-35.9-77.7-64.1-124.3-83.8-48.2-20.3-99.4-30.7-152.2-30.7z"
                     fill="#8f8f8f" p-id="6443"></path>
                  <path d="M652.2 423.3m-54.7 0a54.7 54.7 0 1 0 109.4 0 54.7 54.7 0 1 0-109.4 0Z" fill="#8f8f8f"
                     p-id="6444"></path>
                  <path d="M370.5 423.3m-54.7 0a54.7 54.7 0 1 0 109.4 0 54.7 54.7 0 1 0-109.4 0Z" fill="#8f8f8f"
                     p-id="6445"></path>
                  <path
                     d="M511.5 775.9c-42.6 0-84.9-10.4-122.4-30.1-27-14.1-51.5-33.1-72.1-55.5-11.4-12.4-9.5-32 4.2-41.8 11.5-8.2 27.3-6.7 36.9 3.7 16.3 17.8 35.7 32.8 57.1 44 29.9 15.7 62.4 23.6 96.4 23.6 34 0 66.5-8 96.4-23.6 21.4-11.2 40.8-26.2 57.1-44 9.5-10.4 25.4-11.9 36.9-3.7 13.7 9.8 15.6 29.4 4.2 41.8-20.6 22.5-45.1 41.4-72.1 55.5-37.7 19.7-80 30.1-122.6 30.1z"
                     fill="#8f8f8f" p-id="6446"></path>
               </svg>
            </button>
            <div class="controlAreaEmojiGrid">
            </div>
            <div class="EmojiCommonlyUsed">
               <button v-for="(item, index) in this.chatBoxTextData.exposedEmoji" @click="addCharacter(item)">
                  {{ item }}
               </button>
            </div>
         </div>
         <div class="controlAreaSend">
            <button @click="sendComment()" :style="{ 'pointer-events': loadingDisplay ? 'none' : 'auto' }">
               <div v-show="!loadingDisplay">
                  发布
               </div>
               <loadingDynamicEffect v-show="loadingDisplay" :loadingSize="loadingSize" />
            </button>
         </div>
      </div>
   </div>
</template>
<script>
import loadingDynamicEffect from '../loadingDynamicEffect.vue';
import { useCounterStore } from '../../store/axiosStore.js';
export default {
   data() {
      return {
         textareaValue: '',
         emojiListVisible: false,
         loadingDisplay: false,
         loadingSize: {
            size: 18,
            width: "auto",
            height: "auto",
         },
         chatBoxTextData: useCounterStore().configData.component.chatBoxTextData,
      }
   },
   methods: {
      addCharacter(emojiAdd) {
         this.textareaValue += emojiAdd;
      },
      sendComment() {
         this.loadingDisplay = true;
         setTimeout(() => {
            this.$root.messagePopups({
               message: '发送成功',
               Color: 'messageG',
            });
            this.loadingDisplay = false;
         }, 1000);
      }
   },
   components: {
      loadingDynamicEffect
   },
   props: {
      linkName: {
         type: String,
         default: () => (useCounterStore().configData.component.chatBoxTextData.chatBoxText)
      }
   },
}
</script>
<style>
.commentSection {
   padding: 0 1.5rem 1rem 1.5rem;
}

.inputSection {
   padding-top: 0.75rem;
   width: 100%;
   position: relative;
}

.informationSection {
   padding-top: 1rem;
   border-top: 1px solid var(--color-theme-frame2);
   display: grid;
   gap: 0.75rem;
   grid-template-columns: 1fr 1fr 1fr;
}

.controlArea {
   margin-top: 0.5rem;
   display: grid;
   grid-template-columns: 1fr 1fr;
}

.emojiList {
   box-sizing: border-box;
   padding: 1rem;
   height: 14.25rem;
   position: absolute;
   width: 100%;
   display: flex;
   flex-wrap: wrap;
   border-radius: 0.5rem;
   bottom: 0.25rem;
   background-color: var(--color-theme-white);
   box-shadow: 0 0 0.5rem var(--color-theme-grayscale3);
}

.controlAreaSend {
   display: flex;
   justify-content: flex-end;
}

.controlAreaSend button {
   width: 4rem;
}

.controlAreaEmoji {
   display: flex;
   align-items: center;
}

.controlAreaEmojiGrid {
   margin: 0 0.75rem;
   height: 1.25rem;
   border-right: 1px solid var(--color-theme-frame2);
}

.EmojiCommonlyUsed {
   display: flex;
   flex-wrap: wrap;
}

.controlAreaEmoji button {
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

.controlAreaEmoji button:hover {
   background-color: var(--color-theme-grayscale1);
}

.controlAreaEmoji button:active {
   background-color: var(--color-theme-grayscale3);
}

.controlAreaSend button {
   display: flex;
   align-items: center;
   justify-content: center;
   padding: 0.5rem 1rem;
   border-radius: 0.5rem;
   border: 0px;
   background-color: var(--color-theme-blue-3);
   color: var(--color-theme-white);
}

.controlAreaSend button:hover {
   background-color: var(--color-theme-blue-2);
}

.controlAreaSend button:active {
   background-color: var(--color-theme-blue-1);
}

.commentSection input,
.commentSection textarea {
   width: 100%;
   resize: vertical;
   padding: 1rem;
   font-size: 1rem;
   border-radius: 0.5rem;
   border: 1px solid var(--color-theme-frame2);
   box-sizing: border-box;
   transition: border 0.15s;
   color: var(--color-theme-grayscale65);
   font-family: Roboto, Noto, Helvetica, Arial, sans-serif;
}

.commentSection textarea {
   min-height: 10rem;
}

.commentSection input:hover,
.commentSection textarea:hover {
   border: 1px solid var(--color-theme-frame3);
}

.commentSection input:focus,
.commentSection textarea:focus {
   outline: none;
   border: 1px solid var(--color-theme-blue-1);
}

.commentSection input::placeholder,
.commentSection textarea::placeholder {
   color: var(--color-theme-grayscale4);
}

@media (max-width: 750px) {
   .informationSection {
      grid-template-columns: 1fr;
   }

   .controlArea {
      grid-template-columns: 1fr;
   }

   .controlAreaSend button {
      margin-top: 0.75rem;
      width: 100%;
   }
}

.fade-enter-from {
   opacity: 0;
}

.fade-enter-to {
   opacity: 1;
}

.fade-leave-active {
   transition: opacity 0.15s;
}

.fade-enter-active {
   transition: opacity 0.15s;
}

.fade-leave-from {
   opacity: 1;
}

.fade-leave-to {
   opacity: 0;
}
</style>