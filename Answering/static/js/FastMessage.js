import * as FireBase from './FireBase.js';

document.getElementById('FastMessage').addEventListener('submit', async (e)=>{
    e.preventDefault();
    const description = document.getElementById('messageField').innerHTML;
    if (description != ''){
        let tittle = currentDate();
        const counter = await getCount('Fast Message', tittle);
        tittle = `${tittle}${String(counter).padStart(3, '0')}`;
        let register = {'Title': tittle, 'Description': description, 'Date': new Date(), 'Delete Date': new Date(Date.now() + 3600 * 1000), 'Files': []};
        await putRegister('Fast Message', tittle, register);
        document.getElementById('messageField').innerHTML = '';
    }
})

function currentDate(){
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    const month = String(currentDate.getMonth() + 1).padStart(2, '0');
    const day = String(currentDate.getDate()).padStart(2, '0');
    return `${year}${month}${day}`;
}

async function getCount(section, id){
    let count = await getRegister('Counters', section);
    if ((count == null) || (count[id] === undefined)){
        count = {};
        count[id] = 0
    }
    count[id]++;
    await putRegister('Counters', section, count);
    return count[id]
}

async function putRegister(section, id, register){
    await FireBase.putDatum(section, id, register);
}

async function getRegister(section, id){
    let register = null;
    let dataFounded = await FireBase.getDatum(section, id);
    if (dataFounded.exists()){
        register = dataFounded.data();
    }
    return register;
}