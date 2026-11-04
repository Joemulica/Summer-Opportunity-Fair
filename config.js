// Summer Opportunity Fair settings. Paste links here; blank ones show "opening soon".
window.SOF = {
  heroPhoto: "",            // optional: a real photo (e.g. "images/hero.jpg") replaces the illustration
  kitFormId: "",            // Kit form number, from app.kit.com/forms/1234567
  contact: "",              // sponsorship / invoice request form (Tally or Google Forms)
  // One Stripe Payment Link for the table. In Stripe, add the ad sizes and sponsorships
  // to that link as optional items so camps can tick them at checkout.
  // Name products "SOF27 Exhibitor table", "SOF27 Quarter-page ad", etc. for the reconciliation workbook.
  pay: { CHECKOUT: "", PREORDER: "" },  // PREORDER = Stripe link for the $15 directory pre-order ("SOF27 Directory pre-order")
  // After checkout, Stripe should send camps here to submit listing details and ad artwork:
  listingForm: "",
};
