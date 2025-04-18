<template>
   <div class="commentSection">
      <transition name="fade">
         <div class="captchaBox" v-if="captchaBoxDisplay">
            <captcha @passID="sendComment" @close="captchaBoxDisplay = false" />
         </div>
      </transition>
      <div class="informationSection">
         <div><input type="text" placeholder="昵称" v-model="nameValue"></div>
         <div><input type="text" placeholder="网站" v-model="linkValue"></div>
         <div><input type="text" placeholder="邮箱" v-model="emailValue"></div>
      </div>
      <div class="inputSection">
         <transition name="fade">
            <div class="memeList" v-show="memeListVisible">
               <div class="memeListTop">
                  <div class="memeListTopBut" @click="scrollLeft()" v-show="this.memeListTopPosition > 10">
                     <svg t="1719214853631" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="9019" width="18" height="18">
                        <path
                           d="M740.352 849.919l-57.225 59.008-399.479-396.929 399.476-396.924 57.228 59.004-335.872 337.92z"
                           fill="#272636" p-id="9020"></path>
                     </svg>
                  </div>
                  <div class="memeListTopItemBox" ref="memeList">
                     <div v-for="item in this.memeListData" class="memeListTopItem"
                        :style="{ color: item.id == memeIndex ? 'var(--color-theme-blue-1)' : 'var(--color-theme-grayscale65)' }"
                        @click="this.memeIndex = item.id">
                        {{ item.name }}
                     </div>
                  </div>
                  <div class="memeListTopBut" @click="scrollRight()">
                     <svg t="1719214838623" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="8761" width="18" height="18">
                        <path
                           d="M283.648 174.081l57.225-59.008 399.479 396.929-399.476 396.924-57.228-59.004 335.872-337.92z"
                           fill="#2c2c2c" p-id="8762"></path>
                     </svg>
                  </div>
               </div>
               <div class="memeListHr"></div>
               <keep-alive>
                  <div v-for="items in this.memeListData" :key="items.id" v-show="items.id == this.memeIndex"
                     class="memeListItemBox">
                     <div v-for="item in items.memes" :key="item.id" class="memeListItem"
                        @click="addCharacter(':[' + items.url + '/' + item.url + ']:')">
                        <img :src="this.api.url + this.api.comment.meme + '/' + items.url + '/' + item.url"
                           :alt="item.name">
                     </div>
                  </div>
               </keep-alive>
            </div>
         </transition>
         <textarea :placeholder="placeholderData()" v-model="textareaValue"></textarea>
      </div>
      <div class="controlArea">
         <div class="controlAreaEmoji">
            <button @click="memeListVisible = !memeListVisible">
               <svg t="1702548244505" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="6442" width="20" height="20">
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
               <button v-for="item in this.chatBoxTextData.exposedEmoji" @click="addCharacter(item)">
                  {{ item }}
               </button>
            </div>
         </div>
         <div class="controlAreaSend">
            <button @click="captcha" :style="{ 'pointer-events': loadingDisplay ? 'none' : 'auto' }">
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
import loadingDynamicEffect from '@/components/loadingDynamicEffect.vue';
import { axiosStore } from '@/store/axiosStore.js';
import { dataRelayStore } from '@/store/dataRelayStore.js';
import captcha from '@/components/captcha.vue';
export default {
   data() {
      return {
         api: axiosStore().api,
         nameValue: "",
         linkValue: "",
         emailValue: "",
         textareaValue: '',
         memeListVisible: false,
         loadingDisplay: false,
         captchaBoxDisplay: false,
         memeIndex: 1,
         loadingSize: {
            size: 18,
            width: "auto",
            height: "auto",
         },
         memeListData: [],
         chatBoxTextData: dataRelayStore().configData.component.chatBoxTextData,
         memeListTopPosition: 0,
      }
   }, computed: {
      memeItems() {
         return this.memeListData.flatMap(item => item.memes);
      }
   },
   methods: {
      scrollLeft() {
         if (this.memeListTopPosition - 200 < 0) {
            this.memeListTopPosition = 0;
         } else {
            this.memeListTopPosition -= 200;
         }
         this.$refs.memeList.scrollLeft = this.memeListTopPosition;
      },
      scrollRight() {
         const memeList = this.$refs.memeList;
         const maxScrollLeft = memeList.scrollWidth - memeList.clientWidth;
         if (this.memeListTopPosition + 200 > maxScrollLeft) {
            this.memeListTopPosition = maxScrollLeft;
         } else {
            this.memeListTopPosition += 200;
         }
         this.$refs.memeList.scrollLeft = this.memeListTopPosition;
      },
      placeholderData() {
         if (this.linkName.main) {
            return dataRelayStore().configData.component.chatBoxTextData.chatBoxText;
         } else {
            return this.linkName.name;
         }
      },
      addCharacter(memeAdd) {
         this.textareaValue += memeAdd;
         this.memeListVisible = false;
      },
      captcha() {
         this.captchaBoxDisplay = true;
      },
      sendComment(passId) {
         this.loadingDisplay = true;
         this.captchaBoxDisplay = false;
         axiosStore().apiRequest(this.api.url + this.api.comment.commentAdd,
            {
               "link": this.linkValue,
               "name": this.nameValue,
               "email": this.emailValue,
               "rid": this.linkName.rid,
               "pid": this.linkName.uuid,
               "url": this.$route.path,
               "comment": this.linkName.main ? this.textareaValue : this.placeholderData() + "@" + this.textareaValue,
               "passId": passId,
            }, "post")
            .then(data => {
               if (data.status == 200) {
                  let commentData = data.data;
                  this.nameValue = "";
                  this.linkValue = "";
                  this.emailValue = "";
                  this.textareaValue = '';
                  this.commentDataUpdate(
                     {
                        "uuid": commentData.uuid,
                        "date": commentData.date,
                        "link": commentData.link,
                        "name": commentData.name,
                        "email": commentData.email,
                        "avatar": commentData.avatar,
                        "rid": commentData.rid,
                        "pid": commentData.pid,
                        "comment": commentData.comment,
                     }
                  );
                  axiosStore().messagePopupData = [{
                     message: '发送成功',
                     Color: 'messageG',
                  }]
                  this.linkValue, this.nameValue, this.emailValue, this.textareaValue = "";
               }
            })
         this.loadingDisplay = false;
      }
   }, mounted() {
      axiosStore().apiRequest(this.api.url + this.api.comment.memeList)
         .then(data => {
            this.memeListData = data.data;
         })
   },
   components: {
      loadingDynamicEffect,
      captcha,
   },
   props: {
      linkName: {
         type: Object,
         default: () => ({
            name: dataRelayStore().configData.component.chatBoxTextData.chatBoxText,
            uuid: "",
            rid: "",
            main: true,
         })
      },
      commentDataUpdate: {
         type: Function,
         required: true
      }
   },
}
</script>
<style scoped>
.commentSection {
   position: relative;
   padding: 0 0rem 1rem 0rem;
   border-top: 1px solid var(--color-theme-frame2);
}

.captchaBox {
   display: flex;
   justify-content: center;
   align-items: center;
   background-color: rgba(255, 255, 255, 0.8);
   position: absolute;
   width: 100%;
   height: 100%;
   z-index: 1;
}

.inputSection {
   width: 100%;
   position: relative;
   padding-top: 0.75rem;
}

.informationSection {
   gap: 0.75rem;
   display: grid;
   padding-top: 1rem;
   grid-template-columns: 1fr 1fr 1fr;
}

.controlArea {
   display: grid;
   margin-top: 0.5rem;
   grid-template-columns: 1fr 1fr;
}

.memeList {
   width: 100%;
   padding: 1rem 1.25rem;
   bottom: 0.25rem;
   height: 14.25rem;
   flex-wrap: wrap;
   position: absolute;
   border-radius: 0.5rem;
   box-sizing: border-box;
   background-color: var(--color-theme-white);
   box-shadow: 0 0 0.5rem var(--color-theme-grayscale3);
}

.memeListItemBox {
   grid-gap: 0.75rem;
   display: grid;
   max-height: 10rem;
   grid-template-columns: repeat(auto-fill, minmax(4.25rem, 1fr));
   overflow: auto;
}

.memeListItem {
   display: flex;
   align-items: center;
   justify-content: center;
   transition: background-color 0.15s;
   border-radius: 0.5rem;
   overflow: hidden;
}

.memeListItem:hover {
   background-color: var(--color-theme-grayscale1);
}

.memeListItem:hover img {
   transform: scale(1.15);
}

.memeListItem img {
   width: 100%;
   height: 100%;
   object-fit: cover;
   cursor: pointer;
   transition: transform 0.25s;
}

.memeListTop {
   display: flex;
   margin-bottom: 0.5rem;
}

.memeListTopItemBox {
   width: 100%;
   display: flex;
   white-space: nowrap;
   overflow: hidden;
   position: relative;
   scroll-behavior: smooth;
}

.memeListTopContent {
   display: flex;
   flex-grow: 1;
   overflow: hidden;
}

.memeListTopBut {
   display: flex;
   justify-content: center;
   align-items: center;
   z-index: 1;
   background-color: var(--color-theme-white);
   width: 3rem;
   height: 1.55rem;
   border-radius: 0.25rem;
   cursor: pointer;
   transition: left 0.18s ease-in-out, right 0.18s ease-in-out;
}

.memeListTopBut:hover {
   background-color: var(--color-theme-grayscale1);
}

.memeListHr {
   margin-bottom: 0.5rem;
   border-bottom: 1px solid var(--color-theme-frame2);
}

.memeListTopItem {
   display: flex;
   align-items: center;
   cursor: pointer;
   margin-right: 2rem;
   color: var(--color-theme-grayscale65);
   transition: color 0.15s;
   -moz-user-select: none;
   -webkit-user-select: none;
   -ms-user-select: none;
   user-select: none;
}

.memeListTopItem:hover {
   color: var(--color-theme-grayscale6);
}

.controlAreaSend {
   display: flex;
   justify-content: flex-end;
}

.controlAreaSend button {
   width: 5rem;
}

.controlAreaEmoji {
   display: flex;
   align-items: center;
}

.controlAreaEmojiGrid {
   height: 1.25rem;
   margin: 0 0.75rem;
   border-right: 1px solid var(--color-theme-frame2);
}

.EmojiCommonlyUsed {
   display: flex;
   flex-wrap: wrap;
}

.controlAreaEmoji button {
   border: 0px;
   display: flex;
   width: 2.25rem;
   padding: 0.2rem;
   height: 2.25rem;
   font-size: 1.15rem;
   border-radius: 50%;
   align-items: center;
   justify-content: center;
   transition: background-color 0.15s;
   background-color: var(--color-theme-white);
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
      padding: 0.75rem 1rem;
   }

   .commentSection {
      padding: 0 0rem 1rem 0rem;
   }
}


@media (max-width: 1200px) {
   .controlAreaSend button {
      width: 6rem;
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