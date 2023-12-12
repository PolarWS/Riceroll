<template>
    <bodyItem :itemData="this.itemData" />
    <div class="fileBody" v-show="renderBoolean">
        <div class="fileBox" :style="{ height: sortOrderDropdownBox ? 2.27 * sortOrder.length + 'rem' : '2rem' }">
            <div class="fileItem" @click="sortOrderDropdownBox = !sortOrderDropdownBox">
                <div>
                    {{ sortOrder.find(item => item.id === sortOrderSelected).content }}
                </div>
                <div class="fileItemDate">
                    <svg t="1702384724291" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="5123" width="15" height="15">
                        <path
                            d="M65.409221 340.948229c42.307571-35.385928 65.340147-52.599985 106.850563-88.881306 145.652288 142.907781 145.652288 142.907781 339.739704 331.683215 120.79925-111.760386 223.503377-215.061101 339.745844-322.608535 35.456536 31.605835 69.40472 61.860906 106.844423 95.232968-150.207024 139.312906-298.090119 276.471752-448.054619 415.557484-10.259668-9.280364-19.784602-17.652032-29.03529-26.319435L65.409221 340.948229z"
                            fill="#2c2c2c" p-id="5124"></path>
                    </svg>
                </div>
            </div>
            <transition name="fade">
                <div v-show="sortOrderDropdownBox">
                    <div class="fileItem" v-for="(item, index) in this.sortOrder" v-show="sortOrderSelected != item.id"
                        @click="sortOrderClick(item.id)">
                        <div>
                            {{ item.content }}
                        </div>
                    </div>
                </div>
            </transition>
        </div>
        <div v-for="(item, index) in this.filePageData" class="fileBox">
            <div class="fileDate">
                {{ item.label }}
            </div>
            <div v-for="(item, index) in item.content" class="fileItem" @click="articleRedirection(item.id)">
                <div>
                    {{ item.title }}
                </div>
                <div class="fileItemDate">
                    {{ item.date }}
                </div>
            </div>
        </div>
    </div>
    <loadingDynamicEffect v-show="!renderBoolean" />
</template>
<script>
import bodyItem from './bodyItem.vue';
import loadingDynamicEffect from '../loadingDynamicEffect.vue';
import { useCounterStore } from '../../store/axiosStore.js';
export default {
    data() {
        return {
            fileBodyHight: 1,
            renderBoolean: false,
            filePageData: Object,
            sortOrderSelected: "date",
            sortOrderDropdownBox: false,
            sortOrder: [{ "content": "按照日期排序", "id": "date" }, { "content": "按照标签排序", "id": "tag" }]
        }
    },
    mounted() {
        if (this.$route.query.sortOrder == undefined) {
            useCounterStore().apiRequest(this.api.url + this.api.filePage)
                .then(data => {
                    if (data.status == 200) {
                        this.filePageData = data.data;
                        this.renderBoolean = true;
                    } else {
                        this.$root.messagePopups({
                            message: '服务器错误',
                            Color: 'messageY',
                        });
                    }
                })
                .catch(error => {
                    this.$root.myMethod({
                        message: '服务器连接失败',
                        Color: 'messageR',
                    });
                });
        } else {
            this.sortOrderSelected = this.$route.query.sortOrder;
            useCounterStore().apiRequest(this.api.url + this.api.filePage + "?sortOrder=" + this.$route.query.sortOrder + "&content=" + this.$route.query.content)
                .then(data => {
                    if (data.status == 200) {
                        this.filePageData = data.data;
                        this.renderBoolean = true;
                    } else {
                        this.$root.messagePopups({
                            message: '服务器错误',
                            Color: 'messageY',
                        });
                    }
                })
                .catch(error => {
                    this.$root.myMethod({
                        message: '服务器连接失败',
                        Color: 'messageR',
                    });
                });
        }
    },
    methods: {
        sortOrderClick(event) {
            this.renderBoolean = false;
            this.sortOrderSelected = event;
            this.sortOrderDropdownBox = false;
            useCounterStore().apiRequest(this.api.url + this.api.filePage + "?sortOrder=" + event)
                .then(data => {
                    if (data.status == 200) {
                        this.filePageData = data.data;
                        this.renderBoolean = true;
                    } else {
                        this.$root.messagePopups({
                            message: '服务器错误',
                            Color: 'messageY',
                        });
                    }
                })
                .catch(error => {
                    this.$root.myMethod({
                        message: '服务器连接失败',
                        Color: 'messageR',
                    });
                });
        },
        articleRedirection(event) {
            this.$router.push('/articlePage/' + event);
        }
    },
    components: {
        bodyItem,
        loadingDynamicEffect,
    }, props: {
        itemData: Object,
    },
    inject: ['api'],
}
</script>
<style>
.fileBody {
    margin: 0rem 1.5rem 1rem 1.5rem;
}

.fileBox {
    margin-bottom: 1rem;
    padding: 1rem;
    border: 2px solid var(--color-theme-frame1);
    transition: height 0.25s;
    overflow: hidden;
}

.fileDate {
    font-size: 1.5rem;
    font-weight: 550;
    margin-bottom: 0.5rem;
    padding-bottom: 0.25rem;
    border-bottom: 2px solid var(--color-theme-frame1);
}

.fileItem {
    display: grid;
    cursor: pointer;
    padding: 0.5rem;
    grid-template-columns: 5fr 1fr;
    color: var(--color-theme-grayscale6);
    transition: background-color 0.1s, transform 0.1s;
    user-select: none;
}

.fileItem:hover {
    background-color: var(--color-theme-grayscale1);
}

.fileItem:active {
    background-color: var(--color-theme-grayscale2);
    transform: scale(0.99);
}

.fileItemDate {
    text-align: right;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.25s;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>