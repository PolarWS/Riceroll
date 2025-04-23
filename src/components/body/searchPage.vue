<template>
    <bodyItem :itemData="this.itemData">
        <div class="searchPage">
            <div class="searchBox">
                <input type="text" v-model="searchContent" @keyup.enter="search" placeholder="请输入搜索内容" />
                <button class="searchBut" @click="search">
                    <svg t="1716223247881" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="4350" width="15" height="15">
                        <path
                            d="M283.648 174.081l57.225-59.008 399.479 396.929-399.476 396.924-57.228-59.004 335.872-337.92z"
                            fill="#272636" p-id="4351"></path>
                    </svg>
                </button>
            </div>
            <div class="searchResults">
                <div class="searchItem" v-for="item in searchResults" :key="item.id"
                    @click="articleRedirection(item.id)">
                    <div class="searchTitle" v-html="highlightMatch(item.title)"></div>
                    <div class="searchContent" v-html="highlightMatch(item.content)"></div>
                </div>
            </div>
            <loadingDynamicEffect v-show="loadingDisplay" />
            <div class="searchEmpty" v-show="emptyDisplay">
                <img src="@/assets/image/null.webp" alt="null">
            </div>
            <pagination :pageMax="this.pageMax" :page="this.page" @pageChange="pageChange"
                v-show="searchResults && searchResults.length > 0" />
        </div>
    </bodyItem>
</template>
<script>
import bodyItem from '@/components/body/bodyItem.vue';
import loadingDynamicEffect from '@/components/loadingDynamicEffect.vue';
import pagination from '@/components/pagination.vue';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            pageMax: 1,
            page: 1,
            page_size: 10,
            searchResults: [],
            searchContent: "",
            searchContentTemp: "",
            loadingDisplay: false,
            emptyDisplay: true,
        }
    }, methods: {
        search() {
            this.$router.push({ path: '/searchPage', query: { search: this.searchContent } });
            this.searchContentTemp = this.searchContent;
        },
        searchRequest() {
            this.loadingDisplay = true;
            this.searchResults = [];
            if (this.searchContent === "") {
                this.emptyDisplay = true;
                this.loadingDisplay = false;
                return;
            }
            axiosStore().apiRequest(axiosStore().api.url + axiosStore().api.searchPage, {
                "keyword": this.searchContent,
                "page": this.page,
                "page_size": this.page_size
            }).then(data => {
                if (data.data.length === 0) {
                    this.emptyDisplay = true;
                } else {
                    this.emptyDisplay = false;
                    this.searchResults = data.data;
                }
                this.pageMax = data.pages;
                this.loadingDisplay = false;
            });
        }, pageChange(page) {
            this.page = page;
            this.searchRequest();
        }, articleRedirection(id) {
            this.$router.push({ path: '/articlePage/' + id });
        }, highlightMatch(text) {
            if (!this.searchContentTemp || !text) return text;
            const regex = new RegExp(this.searchContentTemp, 'gi');
            return text.replace(regex, match => `<span>${match}</span>`);
        }
    }, watch: {
        '$route'(to, from) {
            this.searchRequest();
        }
    }, mounted() {
        this.searchContent = this.$route.query.search;
        if (this.searchContent) {
            this.searchRequest();
        }
    },
    components: {
        bodyItem,
        pagination,
        loadingDynamicEffect,
    }, props: {
        itemData: Object,
    }
}
</script>
<style>
.searchPage {
    padding: 0 1.5rem;
}

@media screen and (max-width: 600px) {
    .searchPage {
        padding: 0 1rem;
    }
}

.searchBox {
    gap: 1rem;
    display: grid;
    overflow: hidden;
    padding: 0.5rem 1rem;
    align-items: center;
    margin-bottom: 2rem;
    grid-template-columns: 1fr 3rem;
    border: 2px solid var(--color-theme-frame1);
    border-radius: 0.25rem;
}

.searchBox input {
    border: none;
    padding: 0.5rem 0.5em;
    font-size: 15px;
    transition: background-color 0.3s;
    background-color: var(--color-theme-white);
    border-radius: 0.25rem;
}

.searchBox input:focus {
    outline: none;
}

.searchBut {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: background-color 0.3s;
    border-radius: 0.25rem;
    cursor: pointer;
    border: none;
    background-color: var(--color-theme-white);
}

.searchBut:hover,
.searchBox input:hover {
    background-color: var(--color-theme-grayscale1);
}

.searchBut:active {
    background-color: var(--color-theme-grayscale3);
}

.searchBut:active svg {
    transform: scale(0.99);
}

.searchResults {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.searchItem {
    padding: 1rem;
    border: 2px solid var(--color-theme-frame1);
    transition: height 0.25s;
    overflow: hidden;
    border-radius: 0.25rem;
    cursor: pointer;
    user-select: none;
    transition: background-color 0.15s;
}

.searchItem:hover {
    background-color: var(--color-theme-grayscale1);
}

.searchItem:active {
    background-color: var(--color-theme-grayscale2);
}

.searchItem:active {
    transform: scale(0.99);

}

.searchTitle {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    padding-bottom: 0.25rem;
    border-bottom: 2px solid var(--color-theme-frame1);
}

.searchContent {
    padding: 0.5rem;
    color: var(--color-theme-grayscale6);
}

.searchEmpty {
    margin: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 1.5rem;
    color: var(--color-theme-blue-3);
}

.searchEmpty img {
    width: 30rem;
    height: 30rem;
}

.searchItem span {
    color: var(--color-theme-white);
    background-color: var(--color-theme-blue-3);
    border-radius: 0.15rem;
}
</style>