const express = require('express');
const app = express();
const PORT = 1234;
const cors = require('cors');

app.use(cors());
app.use(express.json());

const HoloJP0 = [
    {
        id: 1,
        name: "Tokino Sora",
        image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1bNQAbJirVX-VpA_GXn91PBsCngGLaAgIqA&s",
        detail: "Soda Chan",
        moreDetail: "Soda Chan the most seiso.",
    },
    {
        id: 2,
        name: "Azki",
        image: "https://yt3.googleusercontent.com/so69WMDlrSwil0013l7MLKIBLV--U_zjya2tG9_Sgij5NBm7raSvbZXUJiiAbQgrZosseqKDobM=s900-c-k-c0x00ffffff-no-rj",
        detail: "Guessu!",
        moreDetail: "Azki like to guessu.",
    },
    {
        id: 3,
        name: "Sakura Miko",
        image: "https://thicc-af.mywaifulist.moe/pending/waifus/nOcPlBoh6HHN7tFJNX2t4OS40P5wY7jC4RUEAgHQ.jpg",
        detail: "Elite Miko",
        moreDetail: "Elite language.",
    },
    {
        id: 4,
        name: "Hoshimachi Suisei",
        image: "https://us-tuna-sounds-images.voicemod.net/f97c5289-5a92-489b-8521-3baad4a1d780-1681966605372.jpg",
        detail: "boar....",
        moreDetail: "That is front or bac....",
    },
    {
        id: 5,
        name: "Robocco",
        image: "https://hololist.net/wp-content/uploads/2022/02/roboco-portrait-66-300x300.jpg",
        detail: "Pon robot",
        moreDetail: "Super pon robot.",
    },
]

// const HoloJP1 = [
    
// ]

const HoloMyth = [
    {
        id: 6,
        name: "Gawr Gura",
        image: "https://yt3.googleusercontent.com/j7klv_42absugu3dCe75LKoRE40VzhpxVGj-NJuz_i2-shLmNpUZp2Fe3t_r8MOccx95gurIeA=s900-c-k-c0x00ffffff-no-rj",
        detail: "A",
        moreDetail: 'This is a pon shark.',
    },
    {
        id: 7,
        name: "Amelia Watson",
        image: "https://external-preview.redd.it/mV9QWMh1TSPtC3G5Qw0iZ6qguC2irmWaGgHBSdvZh-U.jpg?auto=webp&s=d58edf6aa0956f84043cca6572ae672cdf7ed51a",
        detail: "Ame",
        moreDetail: "Don't give her gun.",
    },
    {
        id: 8,
        name: "Calliope Mori",
        image: "https://ih1.redbubble.net/image.2743609345.8861/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg",
        detail: "Cal li o pe",
        moreDetail: "Dinner or bath or Cal li o pe. Daddy's Kobo",
    },
    {
        id: 9,
        name: "Takanashi Kiara",
        image: "https://media.tenor.com/0OX_xi_3r2gAAAAe/takanashi-kiara.png",
        detail: "Pheonix",
        moreDetail: "Mommy's Kobo",
    },
    {
        id: 10,
        name: "Ninomae Ina'nis",
        image: "https://ih1.redbubble.net/image.2826600767.0890/flat,750x,075,f-pad,750x1000,f8f8f8.jpg",
        detail: "Introvert tako",
        moreDetail: "the most introvert tako.",
    },
]

const Hololive = [...HoloJP0, ...HoloMyth];

app.get("/HoloMyth", (req, res) => {
    res.status(200).json(HoloMyth);
})
app.get("/HoloJP0", (req, res) => {
    res.status(200).json(HoloJP0);
})
app.get(`/Hololive`, (req, res) => {
    res.status(200).json(Hololive);
})
app.get("/detail/:name", (req, res) => {
    const { name } = req.params;
    const vtuber = Hololive.find(v => v.name === name);
    if (vtuber) {
        res.status(200).json(vtuber);
    } else {
        res.status(404).json({message : "Vtuber not found"});
    }
});


app.listen(PORT, () => console.log('Server is running.'))