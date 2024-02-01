# DARK_PATTERN_EXTENSION
Darkension is a one-stop solution uniquely designed to identify 23 types of dark patterns through our extension
REPORT
INTRODUCTION
Darkension is a one-stop solution uniquely designed to identify 23 types of dark patterns through our extension.
TYPES OF DARK PATTERNS WE IDENTIFY
1.Urgency: Creating a false sense of urgency to prompt quick decision-making, often by displaying countdowns or limited time offers.
2. Bait and Switch: Advertising a product or service at a low price, only to push users towards a more expensive alternative.
3.Scarcity: Indicating that a product or service is in short supply to encourage quick actions by users afraid of missing out.
4.Misdirection: Intentionally diverting a user's attention away from something, typically to encourage a particular action without the user realizing it.
5.Social Proof: Presenting information to suggest that others are engaging in a particular behaviour, influencing users to follow suit.
6.Subscribe Trap: Tricking users into subscribing to services or newsletters by making it difficult to opt-out or using confusing language.
7.Nagging: Continuously reminding or pressuring users to take a specific action, creating annoyance to increase compliance.
8.Drip Pricing: Revealing additional charges gradually during the checkout process, leading users to spend more than they initially intended.
9.Misleading Information: Providing false or deceptive information to influence user decisions.
10.Hidden Fees: Concealing extra costs until late in the buying process, catching users off guard.
11.Roach Motel: Making it easy for users to get into a situation but difficult for them to get out, such as complicated cancellation processes.
12.Privacy Zuckering: Misleading users into sharing more personal information than they intended, named after Mark Zuckerberg.
13.Trick Questions: Using confusing or ambiguous language in questions to manipulate user responses or choices.
14.Friend Spam: Encouraging users to share content or invite friends through deceptive means, often without clear consent.
15.Disguised Ads: Making advertisements look like regular content to trick users into clicking on them.
16.Obstruction: Intentionally creating obstacles to make it difficult for users to perform certain actions, such as unsubscribing.
17.Sneaking: Making changes to user settings or preferences without clear notification or consent.
18.Forced Action: Compelling users to take a specific action without providing a meaningful alternative.
19.Sneak into Basket: Adding extra items to a user's shopping basket without clear consent.
20.Price Comparison Prevention: Making it difficult for users to compare prices with competitors, often by hiding relevant information.
21.Forced Continuity: Automatically enrolling users in a subscription or service without clear consent.
22.Confirmshaming: Using guilt or social pressure to manipulate users into a specific action, often by framing opt-out choices negatively.
23. Not Dark Pattern: This is not a dark pattern. It's included for reference.

UNIQUENESS AND INNOVATION 
1. Holistic Approach:
The script takes a comprehensive approach by integrating machine learning, natural language processing (NLP), web scraping and numerous python libraries which enhance our product. This holistic methodology enables a more thorough analysis of web content, capturing both structural and semantic features.
2. Real-time Analysis with Web Scraping:
The incorporation of web scraping allows the model to perform real-time analysis on live websites. This feature is innovative because it enables the model to adapt to evolving web content and respond to changes in dark pattern strategies over time.
3. Dynamic Feature Extraction using NLP:
The use of spaCy for NLP analysis provides dynamic and detailed linguistic features from the text. This dynamic extraction of entities, tokens, part-of-speech tags, and dependencies contributes to the model's ability to understand the intricacies of language, making it more robust in detecting nuanced dark patterns.


4. Hyperparameter Tuning with Grid Search
The script employs a grid search approach for hyperparameter tuning of the SVC model. This systematic exploration of hyperparameter space is innovative as it automates the process of finding the best configuration, thus improving the time complexity of our product. In turn increasing the model’s overall performance.
5. Dark Pattern Identification
   - The script goes beyond binary classification by attempting to identify specific dark patterns present in the text. By leveraging a reference column from the training dataset, it adds an innovative layer of interpretability to the model's predictions, allowing users to understand not only whether a dark pattern is present but also the type of pattern.
6. Result Visualization and Analysis
   - The script creates a Pandas DataFrame to organize and present the results in a structured manner. The output includes not only predictions but also detailed information such as the analysed text, identified dark patterns, and its certain type. This organized presentation facilitates further analysis and interpretation.

7. User Interaction
The script allows user interaction by prompting the user to input a website URL for analysis. This interactive feature is innovative as it extends the usability of the script beyond batch processing, enabling users to analyse specific websites of interest in real time.
8. Save and Review Functionality
The script innovatively saves correct predictions along with identified dark patterns to an Excel file. This feature is valuable for users who want to review and analyse instances where the model performed well, providing transparency, and facilitating further investigation.
9.Code is open sourced
Open sourcing code offers numerous advantages by fostering community collaboration, rapid development, and knowledge sharing among developers. It allows for increased security through collective scrutiny, provides flexibility for customization, and establishes a strong support network. The transparency of open-source projects builds trust among users, while the cost-effective nature enables organizations to leverage existing code. Additionally, open source promotes longevity and maintenance, ensuring continued innovation through a diverse community of contributors who can collectively enhance and sustain the software over time.



10.Ethical approach
We have conscientiously employed BeautifulSoup, a widely recognized and respected tool for web scraping. Recognizing the importance of ethical considerations in data extraction, BeautifulSoup allowed us to navigate and parse HTML and XML documents with precision, ensuring responsible and respectful data gathering practices. By utilizing this tool, we aimed to prioritize transparency, compliance with website terms of service, and respect for intellectual property rights. BeautifulSoup not only facilitated our technical requirements for web scraping but also aligned seamlessly with our commitment to ethical standards, reinforcing the ethical foundation of our project.
11.Data set is versatile
Our dataset stands out for its versatility as it extends beyond merely encompassing instances of dark patterns; we meticulously curated it to include examples of what does not qualify as a dark pattern. This comprehensive approach allows our model to not only recognize deceptive design practices but also distinguish between ethical and non-manipulative elements in user interfaces. By incorporating both positive and negative instances, we have equipped our system with a nuanced understanding of digital design, fostering a more robust and accurate identification of dark patterns. This holistic dataset ensures that our model is well-trained to make informed and reliable assessments, contributing to the effectiveness and ethical soundness of our solution.
12. Mitigating interface interference
To address and mitigate interface interference, we have strategically incorporated an additional extension known as the "Ad Blocker" into our system. This specialized extension effectively alleviates disruptions caused by intrusive pop-up ads. By deploying advanced filtering mechanisms, the Ad Blocker identifies and removes unwanted advertisements, thereby enhancing the overall user experience. This intentional integration aligns with our commitment to providing users with a streamlined and interruption-free interface, ensuring that they can navigate digital spaces without the hindrance of disruptive and often misleading pop-up ads. In doing so, our approach aims to prioritize user satisfaction, minimize distractions, and foster a more user-friendly and efficient online environment.
13.Optimization through a local host 
Our system empowers users with a high degree of customization through a locally hosted environment. By hosting the code locally and open sourcing it, we provide users the flexibility to make modifications tailored to their preferences and specific needs. This decentralized approach allows users to have direct control over the system, fostering a sense of ownership and enabling them to implement changes seamlessly. Hosting locally not only ensures the privacy and security of user data but also facilitates a user-centric experience, 
 


where individuals can adapt the system to align precisely with their choices. This local hosting strategy exemplifies our commitment to user empowerment and the promotion of a personalized, adaptable computing environment.
14. User-friendly: intuitive and easy-to-use.
In our commitment to ensuring a user-friendly and easy-to-use experience, we have developed a comprehensive website that serves as an educational hub on dark patterns. This platform not only enlightens visitors about the concept of dark patterns and their various types but also embodies user-centricity by offering a straightforward and accessible interface. Understanding the significance of user feedback, we have integrated a feature that allows individuals to provide their insights while maintaining complete anonymity. This approach not only promotes a transparent and inclusive learning environment but also prioritizes user engagement, ensuring that the educational content is not only informative but also easily navigable and responsive to user needs.
15.Self executable using a Main.py file
The execution of our system is facilitated through the "main.py" file, allowing users to seamlessly run the program within our system. This central script serves as the entry point, orchestrating various functionalities and ensuring the coherent operation of the entire system. Whether for customization, testing, or regular usage, running the system through the "main.py" file streamlines the user experience, aligning with our commitment to simplicity and ease of use. Additionally, the Main.py file also has a user interface designed by the tkinter package which is the standard Python interface to the Tcl/Tk GUI toolkit. 

16. Cross-Browser Compatibility
 Our commitment to providing a seamless user experience led us to prioritize cross-browser compatibility, ensuring that our system integrates effortlessly with popular browsers. By optimizing compatibility with a variety of browsers, including but not limited to Chrome, Firefox, Safari, and Edge, we guarantee users a consistent and reliable experience across different platforms. The user can confidently engage with our system, knowing that its functionality remains robust, irrespective of the browser they choose. Our emphasis on cross-browser compatibility underscores our dedication to inclusivity and usability, aiming to deliver a uniform and dependable experience for users regardless of their preferred browser.






FUTURE PROOFING
1.Trained a HITL feedback system 
We will implement a Human-in-the-Loop (HITL) feedback system, focusing on training and refining the system through valuable user feedback. This iterative process will include a user-friendly approach, wherein we will ask users to identify specific lines with errors. Subsequently, we will correct the identified lines and seek user confirmation. This iterative process will involve continuous improvement, where user input will play a pivotal role in enhancing the algorithms and overall system performance.
2.AI Chatbot
We plan on developing an Artificial Intelligence (AI) Chatbot that serves as an interactive and responsive interface for users. The AI Chatbot is designed to provide real-time assistance, answer queries, and offer a seamless user experience. Utilizing advanced natural language processing capabilities, it adapts to user inputs, becoming more intelligent and context-aware over time. Together, these features underscore our commitment to creating dynamic and user-centric solutions that evolve through user feedback and harness the capabilities of artificial intelligence.
3.Indic Language Support
Our system will be designed to offer extensive support for Indic languages, ensuring that users in the Indian subcontinent can seamlessly engage with our platform in their preferred language. This will involve incorporating specific functionalities, interfaces, and character sets tailored to languages such as Hindi, Tamil, and others. By prioritizing compatibility with Indic languages, we aim to enhance accessibility and inclusivity, acknowledging the cultural and linguistic diversity within our user community. This commitment underscores our dedication to providing a user-friendly experience that caters to speakers of Indic languages.
4.Cross-Software Compatibility
We have already made a cross-software application which is still in developing stage. Extending our commitment to accessibility and user convenience, we plan to develop a dedicated application that mirrors the functionalities of our website. This cross-software compatibility ensures a consistent and familiar experience for users who prefer a mobile or application-based interface. With the app, users can seamlessly access the same features and information available on the website, offering a unified experience across diverse software platforms. Whether users choose to interact with our system through the website or the dedicated app, they can expect identical functionalities, reinforcing our dedication to providing a versatile and user-centric solution adaptable to various software environments. 
