<template>
    <bodyItem :itemData="this.itemData" ref="itemData">
        <div class="fileBody" v-show="renderBoolean">
            <div class="fileBox" :style="{ height: sortOrderDropdownBox ? 2.27 * sortOrder.length + 'rem' : '2rem' }">
                <div class="fileItem" @click="sortOrderDropdownBox = !sortOrderDropdownBox">
                    <div>
                        {{sortOrder.find(item => item.id === sortOrderSelected).content}}
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
                        <div class="fileItem" v-for="item in this.sortOrder" v-show="sortOrderSelected != item.id"
                            @click="sortUpdate(item.id)">
                            <div>
                                {{ item.content }}
                            </div>
                        </div>
                    </div>
                </transition>
            </div>
            <div v-for="item in this.filePageData" class="fileBox">
                <div class="fileDate">
                    {{ item.label }}
                </div>
                <div v-for="item in item.content" class="fileItem" @click="articleRedirection(item.id)">
                    <div>
                        {{ item.title }}
                    </div>
                    <div class="fileItemDate">
                        {{ item.date.slice(0, 10).replace(/-/g, '/') }}
                    </div>
                </div>
            </div>
        </div>
        <loadingDynamicEffect v-show="(!renderBoolean) || addLoadingDiaplsy" />
    </bodyItem>
</template>
<script>
import bodyItem from '@/components/body/bodyItem.vue';
import loadingDynamicEffect from '@/components/loadingDynamicEffect.vue';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            api: axiosStore().api,
            lastWindowHeight: window.innerHeight,
            renderBoolean: false,
            addLoadingDiaplsy: false,
            isBottom: 0,
            size: 30,
            lastData: "",
            bottomItem: "",
            filePageData: [],
            sortOrderSelected: "date",
            tags: '',
            sortOrderDropdownBox: false,
            sortOrder: [{ "content": "按照日期排序", "id": "date" }, { "content": "按照标签排序", "id": "tag" }]
        }
    },
    mounted() {
        this.updateSorting();
        window.addEventListener('scroll', this.handleScroll);
        window.addEventListener('resize', this.handleResize);
    }, beforeDestroy() {
        window.removeEventListener('scroll', this.handleScroll);
        window.removeEventListener('resize', this.handleResize);
    },
    watch: {
        '$route'(to, from) {
            this.isBottom = 0;
            this.filePageData = [];
            this.updateSorting();
        }
    },
    methods: {
        loadMore() {
            if (this.isBottom != 1) {
                const windowHeight = window.innerHeight;
                this.size = Math.min(Math.floor(windowHeight / 30), 30);
                this.addLoadingDiaplsy = true;
                axiosStore().apiRequest(this.api.url + this.api.filePage, {
                    "className": this.sortOrderSelected,
                    "content": this.tags,
                    "lastData": this.lastData,
                    "size": this.size
                })
                    .then(data => {
                        if (data.status == 200) {
                            this.filePageData = this.filePageData.concat(data.data);
                            this.addLoadingDiaplsy = false;
                            if (data.data.length < this.size) {
                                this.isBottom = 1;
                            }
                            if (data.data.length > 0 && data.data[data.data.length - 1].label) {
                                this.lastData = data.data[data.data.length - 1].label;
                            }
                        }
                    })
            }
        },
        handleScroll() {
            if (!this.addLoadingDiaplsy && this.isBottom != 1) {
                const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
                const windowHeight = document.documentElement.clientHeight;
                const scrollHeight = document.documentElement.scrollHeight;

                if (scrollTop + windowHeight >= scrollHeight - 10) {
                    this.loadMore();
                }
            }
        },
        handleResize() {
            const windowHeight = window.innerHeight;
            this.size = Math.floor(windowHeight / 30);
            if (this.$refs.itemData && (window.innerHeight > this.lastWindowHeight) && this.$refs.itemData.$el.clientHeight < windowHeight) {
                this.loadMore();
            }
            this.lastWindowHeight = window.innerHeight;
        },
        sortUpdate(sort) {
            this.isBottom = 0;
            this.filePageData = [];
            if (this.class == "tag") {
                this.lastData = "";
                this.$router.push({ path: '/filePage', query: { class: sort, content: this.tags } });
            } else {
                this.lastData = new Date().getFullYear() + 1;
                this.$router.push({ path: '/filePage', query: { class: sort } });
                this.tags = '';
            }
        },
        updateSorting() {
            this.sortOrderDropdownBox = false;
            this.renderBoolean = false;
            if (this.$route.query.class !== undefined) {
                this.sortOrderSelected = this.$route.query.class;
                if (this.$route.query.content !== undefined) {
                    this.tags = this.$route.query.content;
                } else {
                    this.tags = '';
                }
            } else {
                this.sortOrderSelected = "date";
            }
            if (this.sortOrderSelected == "tag") {
                this.lastData = "";
            } else {
                this.lastData = new Date().getFullYear() + 1;
            }
            this.loadMore();
            this.renderBoolean = true;
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
}
</script>
<style>
.fileBody {
    margin: 0rem 1.5rem 1rem 1.5rem;
    animation-name: fadeIn;
    animation-duration: 0.5s;
}

@media screen and (max-width: 600px) {
    .fileBody {
        margin: 0rem 1rem 1rem 1rem;
    }
}

.fileBox {
    margin-bottom: 1rem;
    padding: 1rem;
    border: 2px solid var(--color-theme-frame1);
    transition: height 0.25s;
    overflow: hidden;
    border-radius: 0.25rem;
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

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}
</style>