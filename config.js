// Summer Opportunity Fair settings. Paste links here; blank ones show "opening soon".
window.SOF = {
  heroPhoto: "",            // optional: a real photo (e.g. "images/hero.jpg") replaces the illustration
  kitFormId: "",            // Kit form number, from app.kit.com/forms/1234567
  contact: "mailto:joe@summeropportunityfair.com",   // sponsorship / invoice requests (swap for a form link later)
  // One Stripe Payment Link for the table. In Stripe, add the ad sizes and sponsorships
  // to that link as optional items so camps can tick them at checkout.
  // Name products "SOF27 Exhibitor table", "SOF27 Quarter-page ad", etc. for the reconciliation workbook.
  pay: {
    TABLE: "https://buy.stripe.com/dRm00jeLYf3i6nIbh98og06",
    QUARTER: "https://buy.stripe.com/aFa00javIcVadQagBt8og05",
    HALF: "https://buy.stripe.com/cNi7sL6fsf3i3bw4SL8og04",
    FULL: "https://buy.stripe.com/7sY4gz47k1cs6nI70T8og03",
    PREORDER: "https://buy.stripe.com/14AfZh8nAaN2bI20Cv8og00",
    GOLD: "https://buy.stripe.com/fZu14n8nA3kA7rM4SL8og02",
    PLATINUM: "https://buy.stripe.com/9B6aEXdHUf3i9zU70T8og01"
  },  // PREORDER = Stripe link for the $15 directory pre-order ("SOF27 Directory pre-order")
  // After checkout, Stripe should send camps here to submit listing details and ad artwork:
  listingForm: "",
};
