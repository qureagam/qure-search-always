console.log(`
This is a browser feature intended for developers. If someone told you to copy-paste something here to enable an QURE feature or "hack" something, it is a scam.`);

const qured_pol = (setting_href)=>{
    window.location.href = `/${setting_href}`;
}
const service_button = document.querySelector("#policy_");
service_button.addEventListener('click',()=>{
    qured_pol("more");
});

const contact_button = document.querySelector("#contact");
contact_button.addEventListener('click',()=>{
    qured_pol("contact");
});