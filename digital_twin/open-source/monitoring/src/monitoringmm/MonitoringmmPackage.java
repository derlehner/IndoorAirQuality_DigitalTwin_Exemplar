/**
 */
package monitoringmm;

import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;

/**
 * <!-- begin-user-doc -->
 * The <b>Package</b> for the model.
 * It contains accessors for the meta objects to represent
 * <ul>
 *   <li>each class,</li>
 *   <li>each feature of each class,</li>
 *   <li>each operation of each class,</li>
 *   <li>each enum,</li>
 *   <li>and each data type</li>
 * </ul>
 * <!-- end-user-doc -->
 * @see monitoringmm.MonitoringmmFactory
 * @model kind="package"
 * @generated
 */
public interface MonitoringmmPackage extends EPackage {
	/**
	 * The package name.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNAME = "monitoringmm";

	/**
	 * The package namespace URI.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_URI = "http://www.se.jku.at/mosumo/metamodel";

	/**
	 * The package namespace name.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_PREFIX = "at.jku.se.mosumo.core.metamodel.monitoringmm";

	/**
	 * The singleton instance of the package.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	MonitoringmmPackage eINSTANCE = monitoringmm.impl.MonitoringmmPackageImpl.init();

	/**
	 * The meta object id for the '{@link monitoringmm.impl.NamedElementImpl <em>Named Element</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see monitoringmm.impl.NamedElementImpl
	 * @see monitoringmm.impl.MonitoringmmPackageImpl#getNamedElement()
	 * @generated
	 */
	int NAMED_ELEMENT = 0;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int NAMED_ELEMENT__NAME = 0;

	/**
	 * The number of structural features of the '<em>Named Element</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int NAMED_ELEMENT_FEATURE_COUNT = 1;

	/**
	 * The number of operations of the '<em>Named Element</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int NAMED_ELEMENT_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link monitoringmm.impl.MonitorableElementImpl <em>Monitorable Element</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see monitoringmm.impl.MonitorableElementImpl
	 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMonitorableElement()
	 * @generated
	 */
	int MONITORABLE_ELEMENT = 1;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MONITORABLE_ELEMENT__NAME = NAMED_ELEMENT__NAME;

	/**
	 * The feature id for the '<em><b>Topic</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MONITORABLE_ELEMENT__TOPIC = NAMED_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Sync</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MONITORABLE_ELEMENT__SYNC = NAMED_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The number of structural features of the '<em>Monitorable Element</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MONITORABLE_ELEMENT_FEATURE_COUNT = NAMED_ELEMENT_FEATURE_COUNT + 2;

	/**
	 * The number of operations of the '<em>Monitorable Element</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MONITORABLE_ELEMENT_OPERATION_COUNT = NAMED_ELEMENT_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link monitoringmm.impl.MOAgentImpl <em>MO Agent</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see monitoringmm.impl.MOAgentImpl
	 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOAgent()
	 * @generated
	 */
	int MO_AGENT = 2;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_AGENT__NAME = MONITORABLE_ELEMENT__NAME;

	/**
	 * The feature id for the '<em><b>Topic</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_AGENT__TOPIC = MONITORABLE_ELEMENT__TOPIC;

	/**
	 * The feature id for the '<em><b>Sync</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_AGENT__SYNC = MONITORABLE_ELEMENT__SYNC;

	/**
	 * The feature id for the '<em><b>Eclass</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_AGENT__ECLASS = MONITORABLE_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The feature id for the '<em><b>Elements</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_AGENT__ELEMENTS = MONITORABLE_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The number of structural features of the '<em>MO Agent</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_AGENT_FEATURE_COUNT = MONITORABLE_ELEMENT_FEATURE_COUNT + 2;

	/**
	 * The number of operations of the '<em>MO Agent</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_AGENT_OPERATION_COUNT = MONITORABLE_ELEMENT_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link monitoringmm.impl.MOConfigImpl <em>MO Config</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see monitoringmm.impl.MOConfigImpl
	 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOConfig()
	 * @generated
	 */
	int MO_CONFIG = 3;

	/**
	 * The feature id for the '<em><b>Agents</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_CONFIG__AGENTS = 0;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_CONFIG__NAME = 1;

	/**
	 * The feature id for the '<em><b>Namespace</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_CONFIG__NAMESPACE = 2;

	/**
	 * The number of structural features of the '<em>MO Config</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_CONFIG_FEATURE_COUNT = 3;

	/**
	 * The number of operations of the '<em>MO Config</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_CONFIG_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link monitoringmm.impl.MOElementImpl <em>MO Element</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see monitoringmm.impl.MOElementImpl
	 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOElement()
	 * @generated
	 */
	int MO_ELEMENT = 4;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_ELEMENT__NAME = MONITORABLE_ELEMENT__NAME;

	/**
	 * The feature id for the '<em><b>Topic</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_ELEMENT__TOPIC = MONITORABLE_ELEMENT__TOPIC;

	/**
	 * The feature id for the '<em><b>Sync</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_ELEMENT__SYNC = MONITORABLE_ELEMENT__SYNC;

	/**
	 * The feature id for the '<em><b>Properties</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_ELEMENT__PROPERTIES = MONITORABLE_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The number of structural features of the '<em>MO Element</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_ELEMENT_FEATURE_COUNT = MONITORABLE_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The number of operations of the '<em>MO Element</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_ELEMENT_OPERATION_COUNT = MONITORABLE_ELEMENT_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link monitoringmm.impl.MOPropertyImpl <em>MO Property</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see monitoringmm.impl.MOPropertyImpl
	 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOProperty()
	 * @generated
	 */
	int MO_PROPERTY = 5;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_PROPERTY__NAME = MO_ELEMENT__NAME;

	/**
	 * The feature id for the '<em><b>Topic</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_PROPERTY__TOPIC = MO_ELEMENT__TOPIC;

	/**
	 * The feature id for the '<em><b>Sync</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_PROPERTY__SYNC = MO_ELEMENT__SYNC;

	/**
	 * The feature id for the '<em><b>Properties</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_PROPERTY__PROPERTIES = MO_ELEMENT__PROPERTIES;

	/**
	 * The feature id for the '<em><b>Eclass</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_PROPERTY__ECLASS = MO_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The number of structural features of the '<em>MO Property</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_PROPERTY_FEATURE_COUNT = MO_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The number of operations of the '<em>MO Property</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_PROPERTY_OPERATION_COUNT = MO_ELEMENT_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link monitoringmm.impl.MOValueImpl <em>MO Value</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see monitoringmm.impl.MOValueImpl
	 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOValue()
	 * @generated
	 */
	int MO_VALUE = 6;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_VALUE__NAME = MO_ELEMENT__NAME;

	/**
	 * The feature id for the '<em><b>Topic</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_VALUE__TOPIC = MO_ELEMENT__TOPIC;

	/**
	 * The feature id for the '<em><b>Sync</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_VALUE__SYNC = MO_ELEMENT__SYNC;

	/**
	 * The feature id for the '<em><b>Properties</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_VALUE__PROPERTIES = MO_ELEMENT__PROPERTIES;

	/**
	 * The feature id for the '<em><b>EAttribute</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_VALUE__EATTRIBUTE = MO_ELEMENT_FEATURE_COUNT + 0;

	/**
	 * The number of structural features of the '<em>MO Value</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_VALUE_FEATURE_COUNT = MO_ELEMENT_FEATURE_COUNT + 1;

	/**
	 * The number of operations of the '<em>MO Value</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MO_VALUE_OPERATION_COUNT = MO_ELEMENT_OPERATION_COUNT + 0;


	/**
	 * Returns the meta object for class '{@link monitoringmm.NamedElement <em>Named Element</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Named Element</em>'.
	 * @see monitoringmm.NamedElement
	 * @generated
	 */
	EClass getNamedElement();

	/**
	 * Returns the meta object for the attribute '{@link monitoringmm.NamedElement#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see monitoringmm.NamedElement#getName()
	 * @see #getNamedElement()
	 * @generated
	 */
	EAttribute getNamedElement_Name();

	/**
	 * Returns the meta object for class '{@link monitoringmm.MonitorableElement <em>Monitorable Element</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Monitorable Element</em>'.
	 * @see monitoringmm.MonitorableElement
	 * @generated
	 */
	EClass getMonitorableElement();

	/**
	 * Returns the meta object for the attribute '{@link monitoringmm.MonitorableElement#getTopic <em>Topic</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Topic</em>'.
	 * @see monitoringmm.MonitorableElement#getTopic()
	 * @see #getMonitorableElement()
	 * @generated
	 */
	EAttribute getMonitorableElement_Topic();

	/**
	 * Returns the meta object for the attribute '{@link monitoringmm.MonitorableElement#isSync <em>Sync</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Sync</em>'.
	 * @see monitoringmm.MonitorableElement#isSync()
	 * @see #getMonitorableElement()
	 * @generated
	 */
	EAttribute getMonitorableElement_Sync();

	/**
	 * Returns the meta object for class '{@link monitoringmm.MOAgent <em>MO Agent</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>MO Agent</em>'.
	 * @see monitoringmm.MOAgent
	 * @generated
	 */
	EClass getMOAgent();

	/**
	 * Returns the meta object for the reference '{@link monitoringmm.MOAgent#getEclass <em>Eclass</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference '<em>Eclass</em>'.
	 * @see monitoringmm.MOAgent#getEclass()
	 * @see #getMOAgent()
	 * @generated
	 */
	EReference getMOAgent_Eclass();

	/**
	 * Returns the meta object for the containment reference list '{@link monitoringmm.MOAgent#getElements <em>Elements</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Elements</em>'.
	 * @see monitoringmm.MOAgent#getElements()
	 * @see #getMOAgent()
	 * @generated
	 */
	EReference getMOAgent_Elements();

	/**
	 * Returns the meta object for class '{@link monitoringmm.MOConfig <em>MO Config</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>MO Config</em>'.
	 * @see monitoringmm.MOConfig
	 * @generated
	 */
	EClass getMOConfig();

	/**
	 * Returns the meta object for the containment reference list '{@link monitoringmm.MOConfig#getAgents <em>Agents</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Agents</em>'.
	 * @see monitoringmm.MOConfig#getAgents()
	 * @see #getMOConfig()
	 * @generated
	 */
	EReference getMOConfig_Agents();

	/**
	 * Returns the meta object for the attribute '{@link monitoringmm.MOConfig#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see monitoringmm.MOConfig#getName()
	 * @see #getMOConfig()
	 * @generated
	 */
	EAttribute getMOConfig_Name();

	/**
	 * Returns the meta object for the attribute '{@link monitoringmm.MOConfig#getNamespace <em>Namespace</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Namespace</em>'.
	 * @see monitoringmm.MOConfig#getNamespace()
	 * @see #getMOConfig()
	 * @generated
	 */
	EAttribute getMOConfig_Namespace();

	/**
	 * Returns the meta object for class '{@link monitoringmm.MOElement <em>MO Element</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>MO Element</em>'.
	 * @see monitoringmm.MOElement
	 * @generated
	 */
	EClass getMOElement();

	/**
	 * Returns the meta object for the containment reference list '{@link monitoringmm.MOElement#getProperties <em>Properties</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Properties</em>'.
	 * @see monitoringmm.MOElement#getProperties()
	 * @see #getMOElement()
	 * @generated
	 */
	EReference getMOElement_Properties();

	/**
	 * Returns the meta object for class '{@link monitoringmm.MOProperty <em>MO Property</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>MO Property</em>'.
	 * @see monitoringmm.MOProperty
	 * @generated
	 */
	EClass getMOProperty();

	/**
	 * Returns the meta object for the reference '{@link monitoringmm.MOProperty#getEclass <em>Eclass</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference '<em>Eclass</em>'.
	 * @see monitoringmm.MOProperty#getEclass()
	 * @see #getMOProperty()
	 * @generated
	 */
	EReference getMOProperty_Eclass();

	/**
	 * Returns the meta object for class '{@link monitoringmm.MOValue <em>MO Value</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>MO Value</em>'.
	 * @see monitoringmm.MOValue
	 * @generated
	 */
	EClass getMOValue();

	/**
	 * Returns the meta object for the reference '{@link monitoringmm.MOValue#getEAttribute <em>EAttribute</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the reference '<em>EAttribute</em>'.
	 * @see monitoringmm.MOValue#getEAttribute()
	 * @see #getMOValue()
	 * @generated
	 */
	EReference getMOValue_EAttribute();

	/**
	 * Returns the factory that creates the instances of the model.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the factory that creates the instances of the model.
	 * @generated
	 */
	MonitoringmmFactory getMonitoringmmFactory();

	/**
	 * <!-- begin-user-doc -->
	 * Defines literals for the meta objects that represent
	 * <ul>
	 *   <li>each class,</li>
	 *   <li>each feature of each class,</li>
	 *   <li>each operation of each class,</li>
	 *   <li>each enum,</li>
	 *   <li>and each data type</li>
	 * </ul>
	 * <!-- end-user-doc -->
	 * @generated
	 */
	interface Literals {
		/**
		 * The meta object literal for the '{@link monitoringmm.impl.NamedElementImpl <em>Named Element</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see monitoringmm.impl.NamedElementImpl
		 * @see monitoringmm.impl.MonitoringmmPackageImpl#getNamedElement()
		 * @generated
		 */
		EClass NAMED_ELEMENT = eINSTANCE.getNamedElement();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute NAMED_ELEMENT__NAME = eINSTANCE.getNamedElement_Name();

		/**
		 * The meta object literal for the '{@link monitoringmm.impl.MonitorableElementImpl <em>Monitorable Element</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see monitoringmm.impl.MonitorableElementImpl
		 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMonitorableElement()
		 * @generated
		 */
		EClass MONITORABLE_ELEMENT = eINSTANCE.getMonitorableElement();

		/**
		 * The meta object literal for the '<em><b>Topic</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute MONITORABLE_ELEMENT__TOPIC = eINSTANCE.getMonitorableElement_Topic();

		/**
		 * The meta object literal for the '<em><b>Sync</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute MONITORABLE_ELEMENT__SYNC = eINSTANCE.getMonitorableElement_Sync();

		/**
		 * The meta object literal for the '{@link monitoringmm.impl.MOAgentImpl <em>MO Agent</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see monitoringmm.impl.MOAgentImpl
		 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOAgent()
		 * @generated
		 */
		EClass MO_AGENT = eINSTANCE.getMOAgent();

		/**
		 * The meta object literal for the '<em><b>Eclass</b></em>' reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MO_AGENT__ECLASS = eINSTANCE.getMOAgent_Eclass();

		/**
		 * The meta object literal for the '<em><b>Elements</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MO_AGENT__ELEMENTS = eINSTANCE.getMOAgent_Elements();

		/**
		 * The meta object literal for the '{@link monitoringmm.impl.MOConfigImpl <em>MO Config</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see monitoringmm.impl.MOConfigImpl
		 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOConfig()
		 * @generated
		 */
		EClass MO_CONFIG = eINSTANCE.getMOConfig();

		/**
		 * The meta object literal for the '<em><b>Agents</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MO_CONFIG__AGENTS = eINSTANCE.getMOConfig_Agents();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute MO_CONFIG__NAME = eINSTANCE.getMOConfig_Name();

		/**
		 * The meta object literal for the '<em><b>Namespace</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute MO_CONFIG__NAMESPACE = eINSTANCE.getMOConfig_Namespace();

		/**
		 * The meta object literal for the '{@link monitoringmm.impl.MOElementImpl <em>MO Element</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see monitoringmm.impl.MOElementImpl
		 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOElement()
		 * @generated
		 */
		EClass MO_ELEMENT = eINSTANCE.getMOElement();

		/**
		 * The meta object literal for the '<em><b>Properties</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MO_ELEMENT__PROPERTIES = eINSTANCE.getMOElement_Properties();

		/**
		 * The meta object literal for the '{@link monitoringmm.impl.MOPropertyImpl <em>MO Property</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see monitoringmm.impl.MOPropertyImpl
		 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOProperty()
		 * @generated
		 */
		EClass MO_PROPERTY = eINSTANCE.getMOProperty();

		/**
		 * The meta object literal for the '<em><b>Eclass</b></em>' reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MO_PROPERTY__ECLASS = eINSTANCE.getMOProperty_Eclass();

		/**
		 * The meta object literal for the '{@link monitoringmm.impl.MOValueImpl <em>MO Value</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see monitoringmm.impl.MOValueImpl
		 * @see monitoringmm.impl.MonitoringmmPackageImpl#getMOValue()
		 * @generated
		 */
		EClass MO_VALUE = eINSTANCE.getMOValue();

		/**
		 * The meta object literal for the '<em><b>EAttribute</b></em>' reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MO_VALUE__EATTRIBUTE = eINSTANCE.getMOValue_EAttribute();

	}

} //MonitoringmmPackage
