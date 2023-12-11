<template>
    <bodyItem :itemData="this.itemData" />
    <div id="pressed" :style="cardBoxAdaptation.grid">
        <div class="cardBox" v-for="(item, index) in itemData.cardList" @click="linkClick(item.url)">
            <div class="cardImg">
                <img :src="(item.src)" />
                <div class="state" :class="statePing(this.pingData[index])" v-if="itemData.pingSwitch"></div>
            </div>
            <div class="cardContent">
                <div class="title" :style="cardBoxAdaptation.width">{{ item.title }}</div>
                <span class="content" :style="cardBoxAdaptation.width">{{ item.content }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import { useCounterStore } from '../../store/axiosStore.js';
import bodyItem from './bodyItem.vue';
export default {
    data() {
        return {
            pingData: Object,
            cardBoxAdaptation: {
                'grid': {
                    'grid-template-columns': '',
                },
                'width': {
                    width: '',
                },
            },
        };
    },
    components: {
        bodyItem,
    }, props: {
        itemData: Object,
    },
    methods: {
        linkClick(url) {
            window.open(url);
        },
        statePing(delay) {
            if (delay < 50) {
                return "stateG";
            }
            else if (delay < 200) {
                return "stateY";
            }
            else if (delay < 998) {
                return "stateO";
            }
            else {
                return "stateR";
            }
        },
        checkWidth() {
            const element = document.querySelector('#pressed');
            if (element.offsetWidth < 600) {
                this.cardBoxAdaptation.grid['grid-template-columns'] = '1fr';
                this.cardBoxAdaptation.width.width = '10rem';
            }
            else {
                this.cardBoxAdaptation.grid['grid-template-columns'] = 'repeat(2, 1fr)';
                this.cardBoxAdaptation.width.width = '9rem';
            }
        },
    }, mounted() {
        this.checkWidth();
        window.addEventListener('resize', this.checkWidth);
    }, created() {
        useCounterStore().apiRequest(this.api.url + this.api.frindLinkPage)
            .then(data => {
                if (data.status == 200) {
                    this.pingData = data.ping;
                } else {
                    this.$root.messagePopups({
                        message: '服务器错误',
                        Color: 'messageY',
                    });
                }
            })
            .catch(error => {
                this.$root.messagePopups({
                    message: '服务器连接失败',
                    Color: 'messageR',
                });
            });
    }, unmounted() {
        window.removeEventListener('resize', this.checkWidth);
    }, props: {
        itemData: Object,
    }, inject: ['api'],
}
</script>
<style scoped>
.content {
    width: 9rem;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2;
}

.title {
    font-size: 1.35rem;
    font-weight: 520;
    margin-top: 0;
    margin-bottom: 0.5rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.state {
    width: 0.85rem;
    height: 0.85rem;
    border-radius: 50%;
    border: 0.25rem solid var(--color-theme-white);
    position: absolute;
    margin-top: 5rem;
}

.stateG {
    background-color: var(--color-theme-G);
}

.stateY {
    background-color: var(--color-theme-Y);
}

.stateO {
    background-color: var(--color-theme-O);
}

.stateR {
    background-color: var(--color-theme-R);
}

.content {
    color: var(--color-theme-grayscale5);
}

#pressed {
    display: grid;
    gap: 1rem;
    margin: 0 1.5rem 1.5rem 1.5rem;
}

.cardBox {
    display: grid;
    border-radius: 0.55rem;
    height: 9.5rem;
    grid-template-columns: 2fr 3fr;
    justify-content: center;
    border: 2px solid var(--color-theme-frame1);
    cursor: pointer;
    transition: border 0.25s, transform 0.1s;
}

.cardBox:hover {
    border: 2px solid var(--color-theme-grayscale4);
}

.cardBox:active {
    transform: scale(0.96);
}

.cardBox img {
    width: 6rem;
    height: 6rem;
    object-fit: cover;
    border-radius: 50%;
}

.cardContent {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem;
}

.cardImg {
    display: flex;
    align-items: center;
    justify-content: right;
}

/* @media screen and (max-width: 600px) {
    #pressed {
        margin: 0 1rem 1rem 1rem;
    }
} */
</style>
