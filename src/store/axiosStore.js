import { defineStore } from 'pinia'
import axios from 'axios'

export const axiosStore = defineStore('axiosStore', {
    state: () => ({
        messagePopupData: [],
        api: {},
    }),
    actions: {
        async apiRequest(url, data, method = 'get') {
            try {
                let res;
                if (method === 'post') {
                    res = await axios.post(url, data);
                } else {
                    if (data && Object.keys(data).length > 0) {
                        res = await axios.get(url, { params: data });
                    } else {
                        res = await axios.get(url);
                    }
                }
                if (res.data.status == 400) {
                    this.messagePopupData.push({
                        message: res.data.message == undefined ? '请求错误' : res.data.message,
                        Color: 'messageR',
                    });
                }else if(res.data.status == 500){
                    this.messagePopupData.push({
                        message: res.data.message == undefined? '请求失败' : res.data.message,
                        Color:'messageO',
                    });
                }
                return res.data;
            } catch (error) {
                this.messagePopupData.push({
                    message: '请求错误: ' + error.message,
                    Color: 'messageR',
                });
            }
        }
    },
})
